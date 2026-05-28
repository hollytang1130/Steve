# Steve

A chatbot that responds like your coworker Steve.

## Setup

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your_key_here
python app.py
```

Then open http://localhost:5000

## Customizing Steve's personality

Edit the `STEVE_SYSTEM_PROMPT` in `app.py`. Once you export your Zoom chat history,
paste example messages in there to make it sound more like the real Steve.

### Exporting Zoom chat history
1. Go to zoom.us → sign in → **My Profile**
2. In the Zoom desktop app: **Settings → Chat → Export chat history**
3. Or ask your Zoom admin to export from the admin portal
4. Paste excerpts into `STEVE_SYSTEM_PROMPT` as examples of how Steve talks
