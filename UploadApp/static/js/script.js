
// After reordering keyword click Re-Order Key button get  id and the order of new keywords as array list

const update_buttons= document.querySelectorAll('.btn-updt')
for(i=0; i<update_buttons.length; i++){
    update_buttons[i].addEventListener('click',(event)=>{  
        var parent_node=event.target.parentNode
        let keyword_list_id=event.target.id
        let listItem=parent_node.firstElementChild.querySelectorAll('.draggable');
        let keyword_update_list=[]
        listItem.forEach(con=>{
            keyword_update_list.push(con.innerHTML)
    })
    updateKeywordListFunc(keyword_list_id,keyword_update_list)
    })
}
// Iterate container and draggable items with that
const draggable_keywords= document.querySelectorAll('.draggable')
const keywords_container= document.querySelectorAll('.costom-container');


//  Add dragged file opacity 
draggable_keywords.forEach(draggable =>{
    draggable.addEventListener('dragstart',()=>{
       draggable.classList.add('dragging')
    })
    draggable.addEventListener('dragend',()=>{
    draggable.classList.remove('dragging')
     })
})

// Compara dragged item position and insert
keywords_container.forEach(container=>{
    container.addEventListener('dragover',(event)=>{   
        event.preventDefault()
        const getAfterElementX= getDragAfterElementY(container,event.clientY)
        const dragging_item= document.querySelector('.dragging')
      
        if (getAfterElementX== null){
            container.appendChild(dragging_item)
        }
       else{
           container.insertBefore(dragging_item,getAfterElementX)
       }
    })
})

// Get cookie to cominicate with backend

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


var csrftoken=getCookie('csrftoken');

// After getting csrf cookie sending data as JSON object to backend
function updateKeywordListFunc(keyword_list_id, keyword_update_list){
    console.log('keyword_update_list',keyword_update_list)
    var url='/update_keyord_list/';

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
        'X-CSRFToken':csrftoken,},
        body:JSON.stringify({
            keyword_list_id:keyword_list_id,keyword_update_list:keyword_update_list
        })

    }).then((response)=>{       
         return response.json();
    }).then((data)=>{
        if(data.success){
            setTimeout(function(){ location.reload() }, 3000);
            alert(data.message);
        }
        else{
            alert(data.message);
        }
    })

}

// Finding the closest division to use inserBefore attribute
function getDragAfterElementY(container, y){
    const draggableElementArrays=[...container.querySelectorAll('.draggable:not(.dragging)')]
    return draggableElementArrays.reduce( (closest, child)=>{
        const box=child.getBoundingClientRect()
        const offset=y-box.top-box.height/2
        if(offset<0 && offset>closest.offset){
            return {offset:offset, element:child
            }
        }
        else {
            return closest
        }
    },{offset:Number.NEGATIVE_INFINITY}).element
}


