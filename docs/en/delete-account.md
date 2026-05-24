# Request to Delete Your Account — Daily Life Assistant

**Daily Life Assistant** (developer: Havasoft) allows you to request deletion of your **cloud account** (email sign-in) and associated data stored on our backend.

**Last updated:** May 2026

---

## Before you request account deletion

Cloud account features are **optional**. You can use the app locally without an account.

If you only want to erase app data but **keep** your login, use [Request to delete your data](./delete-data.md) instead (Settings → **Clear app data**).

---

## How to request account deletion

Account deletion is processed by email (there is no in-app “delete account” button today).

1. **Optional — prepare in the app**
   - If you joined a **shared book** as a member: open **Settings → Shared book** and **Leave book** first.
   - **Sign out** of your cloud account in **Settings** (optional but recommended).
   - Uninstalling the app alone does **not** delete your cloud account.

2. **Send a deletion request by email**
   - **To:** [cuong.hungduong87@gmail.com](mailto:cuong.hungduong87@gmail.com?subject=Daily%20Life%20Assistant%20-%20Account%20deletion%20request)
   - **Subject:** `Daily Life Assistant - Account deletion request`
   - **Include:**
     - The **email address** of the cloud account you want deleted
     - Confirmation that you want **permanent account deletion**
     - Platform: **Android** or **iOS**
     - Any shared book you **own** (if applicable), so we can process owner teardown correctly

3. **Verification**
   - We may reply from the same support address to confirm the request. Reply to complete verification if asked.

4. **Completion**
   - After verification, we delete the account and associated backend data. We will confirm by email when done.

**Target timeline:** we aim to **acknowledge within 30 days** and complete deletion **as soon as practicable** after verification (typically within **30 days** of a valid request).

---

## What is deleted

When your cloud account is deleted, we remove (or anonymize where required):

- Your **cloud login** (email authentication record)
- **Profile / user mirror** linked to that account on our backend (Supabase)
- **Ledger and app data** stored for your account on our backend (income, expenses, budgets, savings, loans, goals, todos, recipes, menus, shopping lists, etc.)
- **Shared book** metadata you **own** (after owner teardown), and your **membership** in books you joined
- **Join requests** and sharing state tied to your account

Data stored **only on your device** is removed when you uninstall the app or use **Clear app data** while signed in; account deletion focuses on **server-side** data tied to your email login.

---

## What is kept

| Data | Reason |
|------|--------|
| **Google Play / App Store** purchase & subscription history | Held by Google / Apple, not by us |
| **Backup files** you exported to Drive, iCloud, etc. | Stored where you saved them — delete manually |
| **Minimal logs** | Short-lived server or security logs only if required by law or abuse prevention; not used to restore your account |

**Premium on device:** local Premium entitlement on a device may remain until you clear app data or reinstall; it is not tied to a restorable cloud account after deletion.

---

## Retention after deletion

- Deleted account credentials and associated app data are **not kept for product use** after deletion is completed.
- Backups and payment records outside our app are subject to **your** Google/Apple account or your own storage policies.

---

## Contact

- **Support email:** [cuong.hungduong87@gmail.com](mailto:cuong.hungduong87@gmail.com)
- **Delete data without deleting account:** [delete-data.md](./delete-data.md)
- **Privacy policy:** [privacy.md](./privacy.md)
