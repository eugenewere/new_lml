(function($) {
  'use strict';
  if ($("#fileuploader").length) {
    $("#fileuploader").uploadFile({
      url: "../../../lmlappassets/images/",
      fileName: "myfile"
    });
  }
})(jQuery);