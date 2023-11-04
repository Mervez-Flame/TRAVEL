Include jQuery 
$(document).ready(function() {
    $("form").submit(function(event) {
        event.preventDefault();
        
        var origin = $("#originSelect").val();
        var destination = $("#destinationSelect").val();

        // Send an AJAX request to your Django view to retrieve flight data
        $.ajax({
            url: "{% url 'get_flight_info' %}",
            method: "GET",
            data: {
                origin: origin,
                destination: destination
            },
            success: function(response) {
                // Display flight information in the HTML using JavaScript
                $("#departureDate").text(response.departure_date);
                $("#arrivalDate").text(response.arrival_date);
                $("#price").text(response.price);
                $("#bookings").text(response.bookings);
                $("#slotsLeft").text(response.slot_left);
            }
        });
    });
});
