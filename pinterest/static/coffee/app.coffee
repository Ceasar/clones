

CATEGORIES = $("#categories")
CATEGORIES_BOTTOM = CATEGORIES.offset().top

$(document).scroll ->
    if $(this).scrollTop() > CATEGORIES_BOTTOM  # user has scrolled past bar
        CATEGORIES.css
            position: "fixed"
            top: "0px"
    else
        # user has not scrolled past
        CATEGORIES.css
            position: "absolute"
            top: "44px"
