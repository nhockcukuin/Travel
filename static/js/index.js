var count = 0;
var itemIcon = Array.from(document.querySelectorAll('.icn'));
var name;
$(

    $('.icon-elliip').click(() => {
        count++;
        if(count % 2 == 1) {

            $('.bar-tools').animate({ width: '4%'})

            $('.body ul li span').css({ display: 'none'})

            $('.box-name-user').css({ display: 'none'})

            $('.box-img-user').animate({ width: '30px', height: '30px', marginTop: '35px'})

            $('.icon').animate({ fontSize: '1.25rem' })

            $('.box-icon-in-out').css({ justifyContent: 'center' })

            for(var i = 0; i < itemIcon.length; i++) {
                name = itemIcon[i].className.slice(-itemIcon[i].className.indexOf('icn')-3, -3).trim();
                itemIcon[i].setAttribute('class', name);
            }

            $('.content').animate({width: '96%'});

        }else {

            $('.bar-tools').animate({ width: '20%'})

            $('.body ul li span').css({ display: ''})

            $('.box-name-user').css({ display: ''})

            $('.box-img-user').animate({ width: '70px', height: '70px', marginTop: ''})

            $('.icon').animate({ fontSize: '1.5rem' })

            $('.box-icon-in-out').css({ justifyContent: 'flex-end' })

            for(var i = 0; i < itemIcon.length; i++) {
                itemIcon[i].setAttribute('class', `${itemIcon[i].className} icn`)
            }

            $('.content').animate({width: '80%'});

        }

    })
)
