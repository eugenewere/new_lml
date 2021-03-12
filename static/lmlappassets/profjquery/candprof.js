$(document).ready(function(){
            $('a[data-toggle="pill"]').on('show.bs.tab', function(e) {

                localStorage.setItem('activeTab', $(e.target).attr('href'));
            });
            var activeTab = localStorage.getItem('activeTab');
            if(activeTab){
                $('#simple-design-tab a[href="' + activeTab + '"]').tab('show');
            }
            $('.cdab').each(function () {
                var attr = $(this).attr('checked');
                 if(typeof attr !== typeof undefined && attr !== false && $(this).val().toLowerCase() === 'disabled' ){

                     if($('#disbledtxtarea:not(:visible)')){
                         console.log('true')
                        $('#disbledtxtarea').css('display', 'block');
                          $('#disbledtxtarea').show();
                    }
                 }
                 else {
                     // {#$('#disbledtxtarea').hide();#}
                 }
            });
        });
ClassicEditor
    .create( document.querySelector( '#bio' ), {
          removePlugins: [  'Image','Table','Media','Image' ],
        toolbar: {
        items: [
          'heading',
          '|',
          'bold',
          'italic',
          '|',
          'bulletedList',
          'numberedList',
          '|',
          'undo',
          'redo'
        ]
      },
    } )
    .then( editor => {
            // console.log( editor );
        const wordCountPlugin = editor.plugins.get( 'WordCount' );
        const wordCountWrapper = document.getElementById( 'word-count' );

        wordCountWrapper.appendChild( wordCountPlugin.wordCountContainer );
    } )
    .catch( error => {
            // console.error( error );
    } );
ClassicEditor
    .create( document.querySelector( '#disability' ), {
          removePlugins: [  'Image','Table','Media','Image' ],
        toolbar: {
        items: [
          'heading',
          '|',
          'bold',
          'italic',
          '|',
          'bulletedList',
          'numberedList',
          '|',
          'undo',
          'redo'
        ]
      },
    } )
    .then( editor => {
            // console.log( editor );
        const wordCountPlugin = editor.plugins.get( 'WordCount' );
        const wordCountWrapper = document.getElementById( 'word-count' );

        wordCountWrapper.appendChild( wordCountPlugin.wordCountContainer );
    } )
    .catch( error => {
            // console.error( error );
    } );

$('.cdab').click(function () {

            if($(this).val().toLowerCase()==='disabled'){

                if($('#disbledtxtarea:not(:visible)')){
                     console.log('true')
                    $('#disbledtxtarea').css('display', 'block');
                     $('#disbledtxtarea').show();
                }
            }else if($(this).val().toLowerCase()==='not_disabled'){
                if($('#disbledtxtarea:visible')){
                    $('#disbledtxtarea').hide();
                }
            }

       });