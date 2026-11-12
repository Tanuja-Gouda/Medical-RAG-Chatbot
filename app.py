
import streamlit as st

from chatbot import ask_question

# 1. Page configuration
st.set_page_config(
    page_title="Medical RAG Chatbot",
    page_icon="🩺",
    layout="centered"
)

# 2. Sidebar
with st.sidebar:

    st.title("🩺 Medical Assistant")

    st.write("Ask questions using our medical knowledge base.")

    if st.button("🗑️ Clear Chat", use_container_width=True):

        st.session_state.messages = []

        st.rerun()

# 3. Main heading
st.title("Medical RAG Chatbot")

st.caption("AI-powered medical information assistant")

st.info(
    "Educational information only. "
    "This chatbot does not replace professional medical advice."
)

# 4. Initialize chat history
if "messages" not in st.session_state:

    st.session_state.messages = []

# 5. Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        # Display sources for assistant messages
        if message["role"] == "assistant":

            sources = message.get("sources", [])

            if sources:

                with st.expander("View Sources"):

                    for source in sources:

                        st.write(
                            f"Document: {source['source']} | "
                            f"Chunk: {source['chunk_number']}"
                        )

# 6. Get user question
question = st.chat_input("Ask your medical question...")

# 7. Process question
if question:

    # Display user message
    with st.chat_message("user"):

        st.markdown(question)

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("Searching medical documents..."):

            try:

                answer, sources = ask_question(question)

                st.markdown(answer)

                with st.expander("View Sources"):

                    for source in sources:

                        st.write(
                            f"Document: {source['source']} | "
                            f"Chunk: {source['chunk_number']}"
                        )

                # Save assistant response
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer,
                    "sources": sources
                })

            except Exception as e:

                error_message = (
                    "Sorry, something went wrong. "
                    "Please try again."
                )

                st.error(error_message)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_message
                })