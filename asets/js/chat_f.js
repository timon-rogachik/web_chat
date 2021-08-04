function change_visibility(id, visibility_to_change = 'unset', display_to_change = 'unset'){
        if (visibility_to_change !== 'unset'){
             document.getElementById(id).style.visibility = visibility_to_change;
             document.getElementById(id).style.display = display_to_change;
        }
        else if (document.getElementById(id).style.visibility === 'hidden'){
            document.getElementById(id).style.visibility = 'visible';
            document.getElementById(id).style.display = display_to_change;
        }
        else {
             document.getElementById(id).style.visibility = 'hidden';
             document.getElementById(id).style.display = 'none';
        }
}

function set_styles(id, change, change2='unset', returned=false){
    document.getElementById(id).style.maxWidth = change;
    document.getElementById(id).style.marginRight = change2;
    if (returned === true){
        document.getElementById(id).style = getComputedStyle(document.getElementById(id))
    }
    console.log(document.getElementById(id).style.maxWidth);


}

function textarea_resize_input(id, id2, dId, pId){
    if (document.getElementById(id).value !== ""){
        document.getElementById(pId).textContent = document.getElementById(id).value
        const len_string = 450;
        let result = document.getElementById(dId).offsetWidth / len_string
        if (document.getElementById(id).rows < 9){
            document.getElementById(id).rows = Math.ceil( result );
            document.getElementById(id).style.marginTop = String( Number (document.getElementById(id).style.marginTop.replace('px', '')) - (Math.ceil( result ) * 20))+'px';
            }
        change_visibility(id2, 'visible');
    }

    else {
       document.getElementById(id).rows = "1";
       document.getElementById(id).style.marginTop = '0px';
       change_visibility(id2, 'hidden');
    }

}

function post_from_enter(id, id2){
    console.log('enter')
    document.getElementById(id).addEventListener('keydown', function(e) {
        if (e.keyCode === 13) {
            document.getElementById(id2).click();
            document.getElementById(id).onChange = true;
        }
    })
}

function CountAndPast(id, id2, text, maximum=470){
    document.getElementById(id2).textContent = text;
    if (document.getElementById(id).offsetWidth < 350){
        document.getElementById(id).marginRight = 3;
    }
    else{
        document.getElementById(id).marginRight = 0;
    }
    let preResult = "";
    let result = "";
    for(i=0; i<text.length; i++){
        if (document.getElementById(id).offsetWidth > maximum){
            result = result + " " + text[i];
            preResult = "";
        }
        else{
            preResult = preResult + text[i];
            result = result + text[i];
        }
        document.getElementById(id2).textContent = preResult;
    }
    document.getElementById(id2).textContent = result;
}


//window.addEventListener('scroll', function() {
//    console.log(pageYOffset + 'px')
//    let y_pos = pageYOffset;
//    if (y_pos >= 380){
//        change_visibility('topBtn', 'visible');}
//
//    else {
//        change_visibility('topBtn', 'hidden');}
//
//    if (y_pos >= 5750){
//        change_visibility('bottomBtn', 'hidden');
//  }
//
//  else {
//        change_visibility('bottomBtn', ' visible')
//  }
//});