function head_color_changer() {
    $("header").css('color', 'red')
}

$("#red_header").on("click", head_color_changer)