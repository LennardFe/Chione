---

<h1 align="center">🔮 Chione</h1>
<p align="center">Python-based autoclicker and macro tool designed primarily for the videogame Minecraft.</p>

---

<h2 align="center">Features</h2>

<div align="justify">
<p>Simple tool for autoclicking and basic macro assistance. It bypasses all well-known clients, functions on any Minecraft version, and remains undetected by major servers. Features include Left- and Right-Click, Auto-Sprint, W-Tap, Strafing, Anti-AFK, and Self-Destruct. In the settings the user can set the option, that all modules halt in menus (incl. inventory & chat) and activate only when Minecraft is in the foreground.</p>
</div>


<h2 align="center">Screenshots</h2>

![image](https://github.com/vs-marshall/Chione/assets/78146861/969a88e3-3075-43bc-b65c-27c3733f4653)
![image](https://github.com/vs-marshall/Chione/assets/78146861/aa3aadd3-877a-46bb-a15e-e8b4ae2dd720)


<h2 align="center">Installation</h2>

<h3 align="center">For Users:</h3>

<div align="center">
<p><b>Follow these steps if you just want to use the tool.</b></p>
</div>

<div align="justify">
<p>Navigate to the <a href="https://github.com/vs-marshall/Chione/tree/main/output">output</a> folder containing the <a href="https://github.com/vs-marshall/Chione/blob/main/output/Chione.exe">Chione.exe</a> file, click on the .exe and then on the three dots at the top right, as shown in the picture below. Then click on <b>download</b>. This is it; the program should work as intended. There is a possibility that your anti-virus program may flag the  .exe as a virus. I can assure you that this is not true; as the code is open source, you can take a look yourself. Enjoy!</p>
</div>

![image](https://github.com/vs-marshall/Chione/assets/78146861/4e87dae6-ab53-4961-ab40-b21b161076a0)

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
$ pip install -r requirements.txt
```

<div align="justify">
<p>You should now be ready to execute the program, navigate to the <i>main.py</i> file and start it. Chione should open itself. <b>In future releases an .exe file will be provided.</b></p>
</div>


<h2 align="center">Additional Information</h2>

<div align="justify">
<p>The code provided in the "Chione" repository on GitHub is freely available for use, modification, and distribution for any purpose. However, it is a requirement to attribute the original source by linking back to the repository and mentioning the author (vs-marshall). Please note that the code is provided without warranty, and the author (vs-marshall) shall not be liable for any damages arising from its use. Use of the code does not imply endorsement or affiliation with the author (vs-marshall) by the users. By accessing and using the code, you agree to these terms.</p>
</div>
