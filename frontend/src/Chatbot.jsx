import './Chatstyles.css';
import react, { useEffect, useState } from 'react';
import {IoMdSend}  from 'react-icons/io';
import {BiBot,BiUser} from 'react-icons/bi';
import axios from "axios";

//The normal url for rasa server is http://localhost:5005/webhooks/rest/webhook   etc... but when dockerised use http://host.docker.internal:5005/webhooks/rest/webhook

function Chatbot(){
    const [chat,setChat] = useState([]);
    const [inputMessage,setInputMessage] = useState('');
    const [botTyping,setbotTyping] = useState(false);


   useEffect(()=>{

        console.log("called");
        const objDiv = document.getElementById('messageArea');
        objDiv.scrollTop = objDiv.scrollHeight;


    },[chat])


    const sessionUpdate = async () => {
        const name = "ghost";
        try {
                const response = await axios.post('http://host.docker.internal:8000/session/', {sender: name});
                const botResponse = JSON.stringify(response.data.messages);

const arrayInput = JSON.parse(botResponse);
const transformed = arrayInput.map((item) => ({
    msg: item.message,
    sender: item.sender,
    sender_id: item.sender === "user" ? "ghost" : undefined
}));

                        console.log("this"+transformed);

                    setChat(transformed)

            } catch (error) {
                console.error("Error communicating with FastAPI:", error);
                setChat([])
            }

        };





    const handleSubmit=(evt)=>{
        evt.preventDefault();
        const name = "ghost";
        const request_temp = {sender : "user", sender_id : name , msg : inputMessage};

        if(inputMessage !== ""){

            setChat(chat => [...chat, request_temp]);
            setbotTyping(true);
            setInputMessage('');
            sendToFastAPI(name,inputMessage);
        }
        else{
            window.alert("Please enter valid message");
        }

    }


        const sendToFastAPI = async (name, msg) => {
            try {
                const response = await axios.post('http://host.docker.internal:8000/chat/', {
                    sender: name,
                    message: msg
                });
                const botResponse = response.data;
                console.log("this is the response "+response)
                console.log("this is the response "+JSON.stringify(response))
                console.log("this is the response data"+JSON.stringify(response.data))

                const response_temp = []; // Initialize an empty array to store all responses

                // Iterate through all bot responses
                botResponse.forEach((response) => {
                response_temp.push({
                    sender: "bot",
                    recipient_id: response.recipient_id,
                    msg: response.message,
                });
                });

                // Process the bot's response and update chat
                console.log("this is the response_temp "+response_temp)
                console.log("this is the response_temp "+JSON.stringify(response_temp))
                setbotTyping(false);
                setChat(chat => [...chat, ...response_temp]);

            } catch (error) {
                console.error("Error communicating with FastAPI:", error);
            }
        };

    console.log(chat);

    const restartChat = async () => {
        const name = "ghost";
    try {
        const response = await axios.post("http://host.docker.internal:8000/restart/", { sender: name });
        console.log(response.data.message); // Log success message
        alert("Chat restarted successfully!");
    } catch (error) {
        console.error("Error restarting chat:", error);
        alert("Failed to restart chat.");
    }
};

    const stylecard = {
        maxWidth : '35rem',
        border: '1px solid black',
        paddingLeft: '0px',
        paddingRight: '0px',
        borderRadius: '30px',
        boxShadow: '0 16px 20px 0 rgba(0,0,0,0.4)'

    }
    const styleHeader = {
        height: '4.5rem',
        borderBottom : '1px solid black',
        borderRadius: '30px 30px 0px 0px',
        backgroundColor: '#8012c4',

    }
    const styleFooter = {
        //maxWidth : '32rem',
        borderTop : '1px solid black',
        borderRadius: '0px 0px 30px 30px',
        backgroundColor: '#8012c4',


    }
    const styleBody = {
        paddingTop : '10px',
        height: '28rem',
        overflowY: 'a',
        overflowX: 'hidden',

    }

    return (
      <div>
        <button onClick={()=>sessionUpdate()}>Try this</button>
        <button onClick={()=>restartChat()}>Restart</button>


        <div className="container">
        <div className="row justify-content-center">

                <div className="card" style={stylecard}>
                    <div className="cardHeader text-white" style={styleHeader}>
                        <h1 style={{marginBottom:'0px'}}>AI Assistant</h1>
                        {botTyping ? <h6>Bot Typing....</h6> : null}



                    </div>
                    <div className="cardBody" id="messageArea" style={styleBody}>

                        <div className="row msgarea">
                            {chat.map((user,key) => (
                                <div key={key}>
                                    {user.sender==='bot' ?
                                        (

                                            <div className= 'msgalignstart'>
                                                <BiBot className="botIcon"  /><h5 className="botmsg">{user.msg || user.message}</h5>
                                            </div>

                                        )

                                        :(
                                            <div className= 'msgalignend'>
                                                <h5 className="usermsg">{user.msg || user.message}</h5><BiUser className="userIcon" />
                                            </div>
                                        )
                                    }
                                </div>
                            ))}

                        </div>

                    </div>
                    <div className="cardFooter text-white" style={styleFooter}>
                        <div className="row">
                            <form style={{display: 'flex'}} onSubmit={handleSubmit}>
                                <div className="col-10" style={{paddingRight:'0px'}}>
                                    <input onChange={e => setInputMessage(e.target.value)} value={inputMessage} type="text" className="msginp"></input>
                                </div>
                                <div className="col-2 cola">
                                    <button type="submit" className="circleBtn" ><IoMdSend className="sendBtn" /></button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>

        </div>
        </div>

      </div>
    );
}

export default Chatbot;
