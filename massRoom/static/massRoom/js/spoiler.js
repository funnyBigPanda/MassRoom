/**
 * Created by Sergiy on 08.08.16.
 */
$(document).ready(function(){
            $('.spoiler-body').hide();
            $('.spoiler-title').click(function(){
                $(this).toggleClass('opened').toggleClass('closed').next().slideToggle();
                if($(this).hasClass('opened')) {
                    $(this).html('Відмінити');
                }
                else {
                    $(this).html('Записатися');
                }
            });
        });