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

function set_styles(id, change, change2='unset', change_int = 0){
    if (change2 === 'unset'){
        change2 = '120px'
    }
    else if (change2 === 'none') {
        change2 = '0px'
    }

    if (change_int < 574){
        document.getElementById(id).style.width = change
        document.getElementById(id).style.marginLeft = change2
        console.log("ааааааааааааааа!!")
    }
    else{
        console.log("неееееет.....")}

}

function textarea_resize_input(id, id2){
    if (document.getElementById(id).value !== ""){
        let len_my_string = document.getElementById(id).value.length;
        const len_string = "аааааааааааааааааааааааааааааааааааааааааааааааа";
        let result = len_my_string / len_string.length
        document.getElementById(id).rows = Math.ceil( result );
        document.getElementById(id).style.marginTop = String( Number (document.getElementById(id).style.marginTop.replace('px', '')) - (Math.ceil( result ) * 20))+'px';
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
        }
    })
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