# PMCIDS = ['4084583', '4164026', '4079914','23788751','24141372','21684626']
# run_retriever(PMCIDS)

import subprocess
import shlex

# Document Retriever Execution Command
# subprocess.call(["python", "main.py"], cwd="docRetriever")

# MedEX Execution Command
command_line = 'java -Xmx1024m -cp lib/*:bin org.apache.medex.Main -i input -o output -b y'
args = shlex.split(command_line)
# subprocess.call(args, cwd="Medex")

# ManTIME execution command
command_line = 'python mantime.py test ../input/ i2b2'
# args = shlex.split(command_line)
# subprocess.call(args, cwd="ManTIME/mantime")

# Rules Execution Command
subprocess.call(["python", "runMain.py"], cwd="RulesForExtraction")
