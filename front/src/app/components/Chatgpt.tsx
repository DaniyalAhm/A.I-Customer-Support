
"use client";

import React from "react";
import { useState } from "react";
import styles from './Chatbot.module.css'
import axios from "axios";
import { useEffect } from 'react';


export default function Chatbot(){
    const [text,setText]= useState([])
    const [botresponse, setbotResponse] = useState('')
    const [userresponse, setuserResponse] = useState('')


    const [loading, setLoading] = useState(false);

        useEffect(() => {

            if(loading){
                axios.get('http://localhost:5000/response',
                    {
                        params:{value: userresponse},
        
                    }
                ).then(function(response){
                    const responseMessage = {text:response.data , user: false};
                    



                    setText([...text,responseMessage]);


                    setLoading(false);
        
                }).catch
                (function(error){ //Semi Colon Since it is a function lol not a dictionary or list
                    console.log(error);
                    const msg =("There was an error processing your request");
                    const responseMessage = {text:msg , user: false};
                    setText([...text, responseMessage]);


                    setLoading(false);

                })}
        
        },[loading]
        
        )




 const handlesubmit = async(event) =>{
        event?.preventDefault();
        
        let Llama = "Llama is loading";
        setuserResponse(event.target[0].value);
        const newMessage=  {text:event.target[0].value , user:true};
        setText([...text, newMessage]);
        event.target[0].value = '';

        await new Promise((resolve) => setTimeout(resolve, 20)); // Adjust this as necessary

        setLoading(true);
 }

return(
<div className={styles.chatcontainer}>
<div className={styles.messages} >
        {text.map((message, index) =>
        
        (
            <p key={index} className={`${styles.message} ${message.user ? styles.user : styles.bot}`}>{message.text}</p>
        )



        )}

    
        
        </div>
      <form onSubmit={handlesubmit} className={styles.form}>
        <input placeholder={'Enter a Message'}
        type='text'
        className={styles.input}
        >
        </input >
        <button type='submit' className={styles.button} >Message</button>
        </form>  
    

 



</div>



)


 }
 