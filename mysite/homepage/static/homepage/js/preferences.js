$(document).ready(function() {
	
	//Hide the preferences saved notification intially
	$('#color_and_text_notification').hide();

	//Bind the save button for the colors and text preferences to show the notification
	$('#color_and_text_btn').click(function(){
		alert('Preferences Updated');
	});

	//Bind the create widget button to display a notification
	$('#create_widget_btn').click(function(){
		alert('Widget Created');
	});

	//Bind the create tab button to display a notification
	$('#create_tab_btn').click(function(){
		alert('Tab Created');
	});

	$('.delete_widget_btn').click(function(){
		$.post("/homepage/modify_preferences/", {save_preferences: 'delete_widget', key: $(this).attr('value')})
		.done(function() {
			alert('Widget Deleted');
		})
		.fail(function() {
			alert('Something is broken');
		})
	});

	$('.delete_tab_btn').click(function(){
		$.post("/homepage/modify_preferences/", {save_preferences: 'delete_tab', key: $(this).attr('value')})
		.done(function() {
			alert('Tab Deleted');
		})
		.fail(function() {
			alert('Something is broken');
		})
	});

});
