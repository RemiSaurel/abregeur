# ✂️ Abregeur

Small project to summarize scientific articles into small `.md` files thanks to GPT API.

## 🤔 Usage
1) Create a `.env` file with your credentials (see the `.env.example` file)
2) Install the requirements with:
```
pip install -r requirements.txt
```
3) Launch the script by passing the path to the markdown file you want to summarize:
```
python3 main.py -f path/to/file.pdf
```
4) The summary will be available in a new `/data` folder with the same name as the original file + `_summary.md`