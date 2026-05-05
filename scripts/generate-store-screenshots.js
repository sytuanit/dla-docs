/* eslint-disable no-console */
const fs = require('fs/promises');
const path = require('path');
const sharp = require('sharp');

const ROOT_DIR = path.resolve(__dirname, '..');
const INPUT_DIR = path.join(ROOT_DIR, 'screenshots');
const ANDROID_INPUT_DIR = path.join(ROOT_DIR, 'screenshots-android');
const IPAD_INPUT_DIR = path.join(ROOT_DIR, 'screenshots-ipad');
const OUTPUT_DIR = path.join(ROOT_DIR, 'screenshots-resized');
const DEFAULT_SELECTION_FILE = path.join(__dirname, 'selected-screenshots.json');
const FILE_REGEX = /^screenshot-.*\.(png|jpg|jpeg|webp)$/i;

const TARGETS = [
  { folder: 'android-1080x1920', width: 1080, height: 1920 },
  { folder: 'ios-1290x2796', width: 1290, height: 2796 },
  { folder: 'ios-1242x2688', width: 1242, height: 2688 },
];

const IPAD_TARGET = { folder: 'ios-2048x2732', width: 2048, height: 2732 };

/** Letterbox color when aspect ratio differs from target (fit: contain) */
const RESIZE_BACKGROUND = '#ffffff';

async function ensureDir(dir) {
  await fs.mkdir(dir, { recursive: true });
}

async function listSourceFiles() {
  const entries = await fs.readdir(INPUT_DIR, { withFileTypes: true });
  return entries
    .filter((entry) => entry.isDirectory())
    .map((entry) => entry.name)
    .sort();
}

async function listLocaleSourceFiles(locale) {
  const localeDir = path.join(INPUT_DIR, locale);
  const entries = await fs.readdir(localeDir, { withFileTypes: true });
  return entries
    .filter((entry) => entry.isFile() && FILE_REGEX.test(entry.name))
    .map((entry) => entry.name)
    .sort();
}

function getSelectionFilePath() {
  const argPath = process.argv[2];
  if (!argPath) return DEFAULT_SELECTION_FILE;

  return path.isAbsolute(argPath)
    ? argPath
    : path.resolve(process.cwd(), argPath);
}

async function loadSelectedScreenshots(selectionFilePath) {
  const raw = await fs.readFile(selectionFilePath, 'utf8');
  const parsed = JSON.parse(raw);
  const candidate = Array.isArray(parsed) ? parsed : parsed?.screenshots;

  if (!Array.isArray(candidate)) {
    throw new Error(
      `Selection JSON must be an array of screenshot filenames (or { "screenshots": [] }): ${selectionFilePath}`
    );
  }

  const selected = [
    ...new Set(
      candidate
        .filter((name) => typeof name === 'string')
        .map((name) => name.trim())
        .filter((name) => name.length > 0)
    ),
  ];

  if (selected.length < 1) {
    throw new Error(
      `Selection JSON must contain at least one screenshot filename. Current count: ${selected.length}`
    );
  }

  const invalidNames = selected.filter((name) => !FILE_REGEX.test(name));
  if (invalidNames.length > 0) {
    throw new Error(
      `Invalid screenshot filenames in selection JSON: ${invalidNames.join(', ')}`
    );
  }

  return selected;
}

async function generateOne(locale, sourceFile, target) {
  const inputRoot = target.folder.startsWith('android') ? ANDROID_INPUT_DIR : INPUT_DIR;
  const inputPath = path.join(inputRoot, locale, sourceFile);
  const outputPath = path.join(OUTPUT_DIR, locale, target.folder, sourceFile);

  await ensureDir(path.dirname(outputPath));

  await sharp(inputPath)
    .resize(target.width, target.height, {
      fit: 'contain',
      background: RESIZE_BACKGROUND,
    })
    .png({ quality: 100 })
    .toFile(outputPath);

  return outputPath;
}

async function listIpadLocales() {
  try {
    const entries = await fs.readdir(IPAD_INPUT_DIR, { withFileTypes: true });
    return entries
      .filter((entry) => entry.isDirectory())
      .map((entry) => entry.name)
      .sort();
  } catch (err) {
    if (err.code === 'ENOENT') return [];
    throw err;
  }
}

async function listIpadLocaleFiles(locale) {
  const localeDir = path.join(IPAD_INPUT_DIR, locale);
  const entries = await fs.readdir(localeDir, { withFileTypes: true });
  return entries
    .filter((entry) => entry.isFile() && FILE_REGEX.test(entry.name))
    .map((entry) => entry.name)
    .sort();
}

async function generateIpadOne(locale, sourceFile) {
  const inputPath = path.join(IPAD_INPUT_DIR, locale, sourceFile);
  const outputPath = path.join(OUTPUT_DIR, locale, IPAD_TARGET.folder, sourceFile);

  await ensureDir(path.dirname(outputPath));

  await sharp(inputPath)
    .resize(IPAD_TARGET.width, IPAD_TARGET.height, {
      fit: 'contain',
      background: RESIZE_BACKGROUND,
    })
    .png({ quality: 100 })
    .toFile(outputPath);

  return outputPath;
}

async function main() {
  try {
    const selectionFilePath = getSelectionFilePath();
    const selectedScreenshots = await loadSelectedScreenshots(selectionFilePath);
    const locales = await listSourceFiles();

    if (locales.length === 0) {
      console.error(`No locale folders found in: ${INPUT_DIR}`);
      console.error('Expected folders like: screenshots/vi, screenshots/en, ...');
      process.exit(1);
    }

    await fs.rm(OUTPUT_DIR, { recursive: true, force: true });
    await ensureDir(OUTPUT_DIR);

    console.log(`Found ${locales.length} locale folder(s) in ${INPUT_DIR}`);
    console.log(`Using selection file: ${selectionFilePath}`);
    console.log(`Selected screenshots (${selectedScreenshots.length}): ${selectedScreenshots.join(', ')}`);
    const results = [];

    for (const locale of locales) {
      const sourceFiles = await listLocaleSourceFiles(locale);
      if (sourceFiles.length === 0) {
        console.warn(`Skipping locale "${locale}" because no screenshot-*.png files were found.`);
        continue;
      }

      const sourceFileSet = new Set(sourceFiles);
      const missingFiles = selectedScreenshots.filter((fileName) => !sourceFileSet.has(fileName));
      if (missingFiles.length > 0) {
        throw new Error(
          `Locale "${locale}" is missing selected screenshots: ${missingFiles.join(', ')}`
        );
      }

      for (const sourceFile of selectedScreenshots) {
        for (const target of TARGETS) {
          const outputPath = await generateOne(locale, sourceFile, target);
          results.push(outputPath);
        }
      }
    }

    const ipadLocales = await listIpadLocales();
    if (ipadLocales.length > 0) {
      console.log(`\nProcessing iPad screenshots from ${IPAD_INPUT_DIR} (${ipadLocales.length} locale(s))`);
      for (const locale of ipadLocales) {
        const ipadFiles = await listIpadLocaleFiles(locale);
        const ipadSelected = ipadFiles.filter((name) => selectedScreenshots.includes(name));
        if (ipadSelected.length === 0) {
          console.warn(
            `Skipping iPad locale "${locale}" — no files matching selection (${selectedScreenshots.join(', ')}).`
          );
          continue;
        }
        for (const sourceFile of ipadSelected) {
          const outputPath = await generateIpadOne(locale, sourceFile);
          results.push(outputPath);
        }
      }
    }

    if (results.length === 0) {
      console.error('No output generated because all locale folders were empty.');
      process.exit(1);
    }

    console.log('\nGenerated store screenshots:');
    results.forEach((p) => console.log(`- ${p}`));
    console.log('\nDone.');
  } catch (error) {
    console.error('Failed to generate screenshots:', error);
    process.exit(1);
  }
}

main();
