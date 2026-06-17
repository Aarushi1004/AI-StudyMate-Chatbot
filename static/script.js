async function sendMessage() {

let input = document.getElementById("userInput");

let message = input.value;


if(message==="") return;


let chatBox = document.getElementById("chatBox");


chatBox.innerHTML += `
<div class="user-message">
${message}
</div>
`;


input.value = "";



let response = await fetch("/chat",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

message:message

})

});



let data = await response.json();



chatBox.innerHTML += `

<div class="bot-message">

${data.reply}

</div>

`;


chatBox.scrollTop =
chatBox.scrollHeight;

}