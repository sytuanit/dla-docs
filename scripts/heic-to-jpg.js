/* eslint-disable no-console */
/**
 * Convert HEIC/HEIF images to JPG (resized & compressed for Word/docx).
 * Usage: node scripts/heic-to-jpg.js [inputDir] [outputDir]
 *   inputDir: folder containing *.HEIC/*.HEIF/*.HEID files (default: current directory)
 *   outputDir: optional (default: dla-docs/scripts/output)
 * Output: JPG max 1200px, quality 80 – suitable for copy-paste into .docx
 */
const fs = require('fs/promises');
const path = require('path');
const convert = require('heic-convert');
const sharp = require('sharp');

const SCRIPT_DIR = path.resolve(__dirname);
const DEFAULT_OUTPUT_DIR = path.join(SCRIPT_DIR, 'output');
const HEIC_REGEX = /\.(heic|heif|heid)$/i;
const MAX_WIDTH = 1200;
const JPEG_QUALITY = 80;

async function ensureDir(dir) {
  await fs.mkdir(dir, { recursive: true });
}

async function findHeicFiles(dir) {
  const entries = await fs.readdir(dir, { withFileTypes: true });
  return entries
    .filter((e) => e.isFile() && HEIC_REGEX.test(e.name))
    .map((e) => path.join(dir, e.name));
}

async function convertOne(inputPath, outputDir) {
  const baseName = path.basename(inputPath, path.extname(inputPath));
  const outputPath = path.join(outputDir, `${baseName}.jpg`);

  const inputBuffer = await fs.readFile(inputPath);
  const decodedBuffer = await convert({
    buffer: inputBuffer,
    format: 'JPEG',
    quality: 1,
  });

  const outputBuffer = await sharp(decodedBuffer)
    .resize(MAX_WIDTH, null, { withoutEnlargement: true })
    .jpeg({ quality: JPEG_QUALITY })
    .toBuffer();

  await fs.writeFile(outputPath, outputBuffer);
  return outputPath;
}

async function main() {
  const inputDir = process.argv[2]
    ? path.resolve(process.cwd(), process.argv[2])
    : process.cwd();

  const outputDir = process.argv[3]
    ? path.resolve(process.cwd(), process.argv[3])
    : DEFAULT_OUTPUT_DIR;

  try {
    const stat = await fs.stat(inputDir);
    if (!stat.isDirectory()) {
      console.error(`Input is not a directory: ${inputDir}`);
      process.exit(1);
    }
  } catch (err) {
    if (err.code === 'ENOENT') {
      console.error(`Input directory not found: ${inputDir}`);
      process.exit(1);
    }
    throw err;
  }

  const heicFiles = await findHeicFiles(inputDir);
  if (heicFiles.length === 0) {
    console.log(`No *.HEIC/*.HEIF/*.HEID files found in: ${inputDir}`);
    process.exit(0);
  }

  await ensureDir(outputDir);

  console.log(`Converting ${heicFiles.length} file(s) → JPG (max ${MAX_WIDTH}px, quality ${JPEG_QUALITY})`);
  console.log(`Input: ${inputDir}`);
  console.log(`Output: ${outputDir}\n`);

  for (const inputPath of heicFiles) {
    try {
      const outputPath = await convertOne(inputPath, outputDir);
      console.log(`  ✓ ${path.basename(inputPath)} → ${path.basename(outputPath)}`);
    } catch (err) {
      console.error(`  ✗ ${path.basename(inputPath)}: ${err.message}`);
    }
  }

  console.log('\nDone.');
}

main().catch((err) => {
  console.error('Failed:', err);
  process.exit(1);
});
