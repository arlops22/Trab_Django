joinha = $("#like > i")
desjoinha = $("#dislike > i")

likes = 3
dislikes = 1

$("#like").click(function(){
    
    if (joinha.hasClass("far fa-thumbs-up") && desjoinha.hasClass("fas fa-thumbs-down")) {
        likes += 1
        dislikes -= 1
        $("#qtdDislike").data("dislikes", dislikes)
        $("#qtdDislike").text($("#qtdDislike").data("dislikes"))

        $("#qtdLike").text($("#qtdLike").data("likes", likes))
        $("#qtdLike").text($("#qtdLike").data("likes"))
        
        $("#dislike > i").removeClass("fas fa-thumbs-down")
        $("#dislike > i").addClass("far fa-thumbs-down")

        $("#like > i").removeClass("far fa-thumbs-up")
        $("#like > i").addClass("fas fa-thumbs-up")

    } else if (joinha.hasClass("far fa-thumbs-up")){
        likes += 1
        $("#qtdLike").data("likes", likes)
        $("#qtdLike").text($("#qtdLike").data("likes"))

        $("#like > i").removeClass("far fa-thumbs-up")
        $("#like > i").addClass("fas fa-thumbs-up")

    } else if (joinha.hasClass("fas fa-thumbs-up")){
        likes -= 1
        $("#qtdLike").data("likes", likes)
        $("#qtdLike").text($("#qtdLike").data("likes"))

        $("#like > i").removeClass("fas fa-thumbs-up")
        $("#like > i").addClass("far fa-thumbs-up")
        
    }       
    
})

$("#dislike").click(function(){

    if (desjoinha.hasClass("far fa-thumbs-down") && joinha.hasClass("fas fa-thumbs-up")) {
        likes -= 1
        dislikes += 1
        $("#qtdDislike").data("dislikes", dislikes)
        $("#qtdDislike").text($("#qtdDislike").data("dislikes"))

        $("#qtdLike").text($("#qtdLike").data("likes", likes))
        $("#qtdLike").text($("#qtdLike").data("likes"))
        


        $("#dislike > i").removeClass("far fa-thumbs-down")
        $("#dislike > i").addClass("fas fa-thumbs-down")

        $("#like > i").removeClass("fas fa-thumbs-up")
        $("#like > i").addClass("far fa-thumbs-up")

    } else if (desjoinha.hasClass("far fa-thumbs-down")){
        dislikes += 1
        $("#qtdDislike").data("dislikes", dislikes)
        $("#qtdDislike").text($("#qtdDislike").data("dislikes"))
        
        $("#dislike > i").removeClass("far fa-thumbs-down")
        $("#dislike > i").addClass("fas fa-thumbs-down")

    } else if (desjoinha.hasClass("fas fa-thumbs-down")){
        dislikes -= 1
        $("#qtdDislike").data("dislikes", dislikes)
        $("#qtdDislike").text($("#qtdDislike").data("dislikes"))

        $("#dislike > i").removeClass("fas fa-thumbs-down")
        $("#dislike > i").addClass("far fa-thumbs-down")

    }

})