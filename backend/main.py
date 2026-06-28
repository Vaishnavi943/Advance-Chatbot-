from langgraph.graph import StateGraph,START, END
from typing import TypedDict, Literal, Annotated
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, BaseMessage
import operator
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver


# state
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


llm = ChatOpenAI()


# defineing nodes
def chat_node(state: ChatState):
    # take user query from state
    messages = state['messages']

    # send to llm
    response = llm.invoke(messages)

    # response store in state
    return {'messages': [response]}


# storing previous messages in ram
checkpointer  = MemorySaver()


# graph
graph = StateGraph(ChatState)


# add nodes
graph.add_node('chat_node', chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)


# compile
chatbot = graph.compile(checkpointer=checkpointer)


# try

thread_id = '1'

while True:
    user_message = input('Type messages: ')

    print("user: ", user_message)
    if user_message.strip().lower() in ['exit', 'quit', 'bye']:
        break
    
    config = {'configurable': {'thread_id': thread_id}}
    # response = chatbot.invoke({'messages': [HumanMessage(content=user_message)]}, config=config)
    for message_chunk, metadata in chatbot.stream(
        {'messages': [HumanMessage(content=user_message)]}, config=config, stream_mode='messages'
    ):
        if message_chunk.content:
            print(message_chunk.content, end=" ", flush=True)
    
    # print("AI: ", response['messages'][-1].content)
















