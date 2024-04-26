---

<h1 align="center">🔮 Chione</h1>
<p align="center">Python-based autoclicker and macro tool designed primarily for the videogame Minecraft.</p>
<p align="center"><a href="https://github.com/vs-marshall/Chione?tab=readme-ov-file#installation">Download & Installation</a></p>

<h2 align="center">Features</h2>

<div align="justify">
<p>Simple tool for autoclicking and basic macro assistance. The program bypasses all well-known clients, functions on any Minecraft version, and remains undetected by servers. Features include Left- and Right-Clicker, Auto-Sprint, SprintReset, Strafing, Anti-AFK, Self-Destruct and a Config-System. The settings provide customizability so you can adjust the program to your likings. Additionally, tooltips should explain all functionality.</p>
</div>


<h2 align="center">Screenshots</h2>

![image](https://github.com/vs-marshall/Chione/assets/78146861/516ddead-0241-46a6-baa0-603ddace95a9)
![image](https://github.com/vs-marshall/Chione/assets/78146861/6919e7b9-3c6d-446d-8d73-b0a2ee8455af)

<h2 align="center">Installation</h2>

<h3 align="center">For Users:</h3>

<div align="center">
<p><b>Follow these steps if you just want to use the tool.</b></p>
</div>

<div align="justify">
<p>Navigate to the <a href="https://github.com/vs-marshall/Chione/tree/main/output">output</a> folder containing the <a href="https://github.com/vs-marshall/Chione/blob/main/output/Chione.exe">Chione.exe</a> file, click on the .exe and then on the three dots at the top right, as shown in the picture below. Then click on <b>download</b>. The download takes a few seconds to start. There is a possibility that your anti-virus program may flag the  .exe as a virus. I can assure you that this is not true; as the code is open source, you can take a look yourself. Enjoy!</p>
</div>

![download](https://github.com/vs-marshall/Chione/assets/78146861/003dd8e3-42ce-4328-b485-798fa47d5a40)

<h3 align="center">For Developers:</h3>

<div align="center">
<p><b>Follow these steps if you would like to make changes to the existing source code.</b></p>
</div>

<div align="justify">
<p>Install Python 3.11.5, ensuring compatibility with the project requirements. Start by navigating to the GitHub page of this project. Locate the green Code button on the top right and click it. You can either clone it using the command prompt with git clone followed by the shown URL, download the zip file, or open it directly with GitHub Desktop. After that navigate to the project folder and continue with the next step.</p>
</div>

<div align="justify">
<p>After setting up Python and having downloaded the project, I would recommend setting up a virtual environment to isolate the project and its packages, to avoid interference with a possible global Python installation. To do that, you can use the following command on any system:</p>
</div>

```
python -m venv .venv
```

<div align="justify">
<p>This will create a new folder called <i>.venv</i> containing the virtual environment. Run the next command to activate the created environment. After running this, you should see the virtual environment's name (.venv) show up in the command prompt.</p>
</div>

```
.venv\Scripts\Activate
```

<div align="justify">
<p>As the last step, install the required packages, which are listed in the <i>requirements.txt</i> with the following command:</p>
</div>

```
pip install -r requirements.txt
```

<div align="justify">
<p>You should now be ready to execute the program, navigate to the <i>main.py</i> file and start it. Chione should open itself.</p>
</div>


<h2 align="center">Additional Information</h2>

<div align="justify">
<p>Please be aware that this work is still in progress. If you encounter any bugs, issues, or have ideas for improvement, please share them under the 'Issues' tab at the top. Additionally, note that the usage of autoclickers and macro tools may be prohibited by some servers. I do not take any responsibility or liability for any consequences resulting from the use of this tool. Use it at your own risk. For more information regarding the usage of the code, please refer to the provided license.</p>
</div>
