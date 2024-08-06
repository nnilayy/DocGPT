CSS = """
<style>
.chat-container {
    display: flex;
    flex-direction: column;
    height: calc(100vh - 200px);
    overflow-y: auto;
    padding-bottom: 70px;
    margin-left: 10px;
    margin-right: 10px;
}
.input-container {
    position: fixed;
    bottom: 0;
    width: 100%;
    background-color: #333;
    padding: 10px 0;
}
.message {
    border-radius: 10px;
    padding: 10px;
    margin: 10px;
    max-width: 60%;
}
.user {
    background-color: #787878;
    margin-left: auto;
    text-align: left;
}
.llm {
    background-color: #3c3c3c;
    margin-right: auto;
    text-align: left;
}
.stTextInput>div>input {
    border-radius: 10px;
    padding: 10px;
    font-size: 16px;
    width: calc(100% - 20px);
    margin: 10px auto;
}
.stButton>button {
    background-color: #25D366;
    color: white;
    font-size: 16px;
    border-radius: 10px;
    margin: 10px auto;
    width: calc(100% - 20px);
}
</style>
"""
