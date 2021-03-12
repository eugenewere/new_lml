



$box = $(".box");
$button = $(".button");

$button.on("click", "", function() {
   console.log("here");
   $self = $(this);

   if($self.attr("data-type") === "sign-up") {
      $box.removeClass("move-right");
      $box.addClass("move-left");
      $box.find(".box-content[data-type=sign-up]").removeClass("hide");
      $box.find(".box-content[data-type=login]").addClass("hide");
   } else {
      $box.addClass("move-right");
      $box.removeClass("move-left");
      $box.find(".box-content[data-type=sign-up]").addClass("hide");
      $box.find(".box-content[data-type=login]").removeClass("hide");
   }
});

