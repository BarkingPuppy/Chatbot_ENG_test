from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
"Terminal",
storage_adapter="chatterbot.storage.SQLStorageAdapter",
logic_adapters=[
			"chatterbot.logic.MathematicalEvaluation",
        	"chatterbot.logic.TimeLogicAdapter",
        	"chatterbot.logic.BestMatch"
    	],
    	input_adapter="chatterbot.input.TerminalAdapter",
    	output_adapter="chatterbot.output.TerminalAdapter",
    	database="../database.db"
	)
chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train('chatterbot.corpus.english')
print("Type something to begin...")

# The following loop will execute each time the user enters input
while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
       		chatbot_input = chatbot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
