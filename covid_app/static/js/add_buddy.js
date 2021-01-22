var buddy = 1;
function buddy_fields() {

    buddy++;
    var objTo = document.getElementById('buddy_fields')
    var divtest = document.createElement("div");
	divtest.setAttribute("class", "form-group removeclass" + buddy);
	var rdiv = 'removeclass' + buddy;


	var extra_buddy = '' +
        '<div class="col-sm-3 nopadding">' +
        '<div class="form-group"> ' +
        '<input type="text" name="buddy[]" id="id_buddy" class="form-control" placeholder="Buddy" autocomplete="off">' +
        '</div></div>' +
        '<button class="btn btn-danger" type="button" onclick="remove_buddy_fields('+ buddy +');"> ' +
        '<span class="glyphicon glyphicon-minus" aria-hidden="true"></span>Remove Buddy</button>' +
        '<div class="col-sm-3 nopadding">' +
        '<div class="clear"></div>';

	divtest.innerHTML = extra_buddy
    objTo.appendChild(divtest)
}
   function remove_buddy_fields(rid) {
	   $('.removeclass'+rid).remove();
   }


        // <!--                    <div id="inputFormRow">-->
        // <!--                        <div class="input-group mb-3">-->
        // <!--                            <input type="text" name="buddy" id="id_buddy" class="m-input" placeholder="Buddy" autocomplete="off">-->
        // <!--                            <div class="input-group-append">-->
        // <!--                                <button id="removeRow" type="button" class="btn btn-danger">Remove</button>-->
        // <!--                            </div>-->
        // <!--                        </div>-->
        //
        // <!--                    <div id="newRow"></div>-->
        // <!--                    <button id="addRow" type="button" class="btn btn-info">Add Buddy</button>-->
        // <!--                </div>-->