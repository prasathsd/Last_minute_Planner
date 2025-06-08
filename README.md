---

## Troubleshooting

- **API errors**: Make sure your OpenAI API key is correct and has access to GPT-4.
- **Weather errors**: If weather info is missing, check your internet connection.
- **Rate limits**: The script waits 1 second between cities to avoid hitting API limits.

---

## Customization

- Change the prompts in the script to get different styles of output.
- Save results in a different format by editing the `save_to_file` function.

---

## License

MIT License.  
You are free to use, modify, and share!

---

## Credits

- Weather data from [wttr.in](https://wttr.in)
- AI completions from [OpenAI](https://openai.com)

## Setting your OpenAI API Key

For security, do **not** put your API key in the code.

Instead, set it as an environment variable before running the script:

**On Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="sk-proj-yourkeyhere"
```

**On Mac/Linux (bash):**
```
export OPENAI_API_KEY=sk-proj-yourkeyhere
```