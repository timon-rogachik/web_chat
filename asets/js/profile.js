function image_input_file(id,id2){
    document.getElementById(id).click();
    let selectedFile = document.getElementById(id).files[0];
    document.getElementById(id2).src = selectedFile

}