# Cal AI Clone — Progress Log

## Project Goal
Build a personal calorie-tracking app (like Cal AI) with AI-powered food image
recognition, focused on accurate Indian food detection. Building it myself to
learn computer vision / AI engineering for resume purposes. Eventual goal:
publish free on Play Store.

## Tech decisions so far
- **AI Provider**: Groq (free tier, no billing required) — using
  `meta-llama/llama-4-scout-17b-16e-instruct` for vision
  - Tried Gemini first — blocked by India billing requiring ₹1000 prepay
  - Tried Anthropic — needs paid credits, no free trial currently
  - Groq works, free, decent accuracy — may revisit Claude/GPT-4o later
    for accuracy comparison once budget allows
- **Language**: Python (backend/AI logic), plan to learn FastAPI next,
  then React Native (Expo) for the mobile app, Supabase for auth+DB
- **Repo**: github.com/i-kshitij/cal-ai-clone

## What's working
- [x] Python venv + VS Code setup
- [x] .env + python-dotenv for API key management
- [x] Basic Groq API text call working
- [x] Image → base64 → sent to vision model → got food description back
      (tested on a thali photo — correctly ID'd chapati, rice, 2 curries,
      gave rough calorie/macro estimates)
- [x] Git + GitHub pushed, .gitignore protecting .env and venv/

## Next steps (in order)
- [ ] Get structured JSON output from the model (dish_name, calories,
      protein_g, carbs_g, fat_g) instead of free text — needed so the app
      can actually parse and store results
- [ ] Test accuracy on 5-10 more Indian food photos, note failure patterns
- [ ] Learn FastAPI, wrap this into an API endpoint
- [ ] Learn React Native (Expo) basics
- [ ] Connect frontend to backend
- [ ] Supabase for auth + saving meal logs
- [ ] Basic dashboard UI (calories left, macros left)
- [ ] Polish + Play Store publish

## Known issues / things to revisit
- Calorie estimates are wide-range guesses (650-850 cal for one meal) —
  portion estimation from a single photo is inherently hard, may need
  better prompting or a reference-object technique later

## Learning notes (syntax/concepts I want to remember)
- Python f-strings: f"text {variable}" for inserting variables into strings
- base64 encoding needed to send images in JSON API calls
- venv keeps project dependencies isolated — activate with
  venv\Scripts\activate on Windows
- .gitignore must be at project ROOT, not nested inside subfolders
- git add . / git commit -m "message" / git push — routine after every
  meaningful change