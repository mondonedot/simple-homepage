//This is the main javascript file
$(document).ready(function() {

	//Bind the delete bookmark buttons to make a request to delete
	//the given bookmark when clicked.
	$('.delete_bookmark_btn').click(function() {
		$.post("/homepage/modify_bookmarks/", {key: $(this).attr('value'), bookmark_request: 'delete'})
		.done(function() {
			console.log('success');
		})
		.fail(function() {
			console.log('fail');
		})
	});

	//Bind the delete button toggle to show the red x's when the user wants to delete.
	//Initially, all of the x's are hidden.
	$('.delete_bookmark_btn').hide();
	$('#delete_bookmark_toggle').click(function(){
		if($(this).attr('value') == 'show') {
			$('.delete_bookmark_btn').fadeIn();
			$(this).fadeOut(function(){
				$(this).text('Finish').fadeIn();
				$(this).css({'background-color': '#ff7272'});
			});
			$(this).attr('value', 'hide');
		} else {
			$('.delete_bookmark_btn').fadeOut();
			$(this).fadeOut(function(){
				$(this).text('Delete Bookmarks').fadeIn();
				$(this).css({'background-color': ''});
			});
			$(this).attr('value', 'show');
		}
	});

	//Slide toggle for the bookmark and widget sections.
	$('#bookmark_toggle_panel').click(function(){
		$('#bookmark-panel-body').slideToggle();
		$(this).text('Show');
	});
	$('#widget_toggle_panel').click(function(){
		$('#widget-panel-body').slideToggle();
		$(this).text('Show');
	});

	//Bind the tabs on the notepad to change the value of the save button.
	//The save will be able to post which page is being saved according to the value.	
	$('.tab_btn').click(function(){
		$('#save_button').attr('value', $(this).attr('id'));
	});

	//Initially hide the save notification button
	$('#save_notification').hide();

	//Bind the save button to perform an ajax post request
	$('#save_button').on('click', function(event) {
		$('#save_notification').fadeIn();
		setTimeout(function(){$('#save_notification').fadeOut();}, 5000);

		console.log('save button clicked');
		event.preventDefault();
		save_notepad();
	});
});

//Function that is called to make the ajax request to save whatever is in the notepad.
function save_notepad() {
	console.log($('div.active > textarea').val());
	console.log($('#save_button').attr('value'));

	$.ajax({
		url: "/homepage/save_notepad/",
		type: "POST",
		data: {content: $('div.active > textarea').val(), content_tab: $('#save_button').attr('value')},

		success: function(json) {
			console.log("Ajax post succesful");
		},
		error: function(xhr, errmsg, err) {
			console.log("Error in ajax request");
		}
	});
}
