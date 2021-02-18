document.addEventListener('DOMContentLoaded',function(){
    document.querySelector('#Adder').style.display="none";
     document.querySelector('#add_question').onclick =count;
});

function count(){
    x= document.querySelector('#Adder');
    if(x.style.display==="none"){
        x.style.display="block";
    }
    else{
        x.style.display="none";
    }
}