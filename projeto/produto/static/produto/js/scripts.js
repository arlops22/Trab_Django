$("form" ).submit(function(e) {
    nome = $("#nome").val();
    email = $("#email").val();
    telefone = $("#telefone").val();
    mensagem = $("#mensagem").val();
    select = $("#select").val()
    radio1 = $("#radio1").prop("checked")
    radio2 = $("#radio2").prop("checked")
    radio3 = $("#radio3").prop("checked")
    check1 = $("#check1").prop("checked")
    check2 = $("#check2").prop("checked")
    check3 = $("#check3").prop("checked")


    if (email != '' && nome != '' && telefone != '' && mensagem != '' && select != "Selecionar produto" && 
        (radio1 === true || radio2 === true || radio3 === true) && (check1 === true || check2 === true || check3 === true)) {

        $( "#warning" ).removeClass( "d-block" );
        $( "#warning" ).addClass( "d-none" );
        alert("Formulário enviado")

    } else {

        $("#nome").addClass("is-invalid");
        $("#email").addClass("is-invalid");
        $("#telefone").addClass("is-invalid");
        $("#mensagem").addClass("is-invalid");
        $("#select").addClass("is-invalid");
        $("#radio1").addClass("is-invalid")
        $("#radio2").addClass("is-invalid")
        $("#radio3").addClass("is-invalid")
        $("#check1").addClass("is-invalid")
        $("#check2").addClass("is-invalid")
        $("#check3").addClass("is-invalid")

        $( "#warning" ).removeClass( "d-none" );
        $( "#warning" ).addClass( "d-block" );

        e.preventDefault();    

    }    
});


/*   VALIDAÇOES DO FORM  */

$("#nome").blur(function(){

    nome = $("#nome").val()
    console.log(nome)


    if (nome == '') {
        $("#nome").addClass("is-invalid");
    } else {
        $("#nome").removeClass("is-invalid");
    }

});


$("#email").blur(function(){

    email = $("#email").val();

    if (email === '') {
        $("#email").addClass("is-invalid");
    }else {
        $("#email").removeClass("is-invalid");
    }

});


$("#telefone").blur(function(){

    telefone = $("#telefone").val()

    if (telefone === '') {
        $("#telefone").addClass("is-invalid");
    }else {
        $("#telefone").removeClass("is-invalid");
    }

});


$("#radio1").click(function(){
    radio = $("#radio1").prop("checked")
    if (radio === true) {
        $("#radio1").removeClass("is-invalid")
        $("#radio2").removeClass("is-invalid")
        $("#radio3").removeClass("is-invalid")
    }
})

$("#radio2").click(function(){
    radio = $("#radio2").prop("checked")
    if (radio === true) {
        $("#radio1").removeClass("is-invalid")
        $("#radio2").removeClass("is-invalid")
        $("#radio3").removeClass("is-invalid")
    }
})

$("#radio3").click(function(){
    radio = $("#radio3").prop("checked")
    if (radio === true) {
        $("#radio1").removeClass("is-invalid")
        $("#radio2").removeClass("is-invalid")
        $("#radio3").removeClass("is-invalid")
    }
})

$("#check1").click(function(){
    check = $("#check1").prop("checked")
    if (check === true) {
        $("#check1").removeClass("is-invalid")
        $("#check2").removeClass("is-invalid")
        $("#check3").removeClass("is-invalid")
    }
})

$("#check2").click(function(){
    check = $("#check1").prop("checked")
    if (check === true) {
        $("#check1").removeClass("is-invalid")
        $("#check2").removeClass("is-invalid")
        $("#check3").removeClass("is-invalid")
    }
})

$("#check3").click(function(){
    check = $("#check1").prop("checked")
    if (check === true) {
        $("#check1").removeClass("is-invalid")
        $("#check2").removeClass("is-invalid")
        $("#check3").removeClass("is-invalid")
    }
})


$("#select").blur(function(){
    select = $("#select").val()

    if (select === "Selecionar produto") {
        $("#select").addClass("is-invalid")
    } else {
        $("#select").removeClass("is-invalid");
    }
})


$("#mensagem").blur(function(){

    mensagem = $("#mensagem").val()

    if (mensagem === '') {
        $("#mensagem").addClass("is-invalid");
    }else {
        $("#mensagem").removeClass("is-invalid");
    }

});
