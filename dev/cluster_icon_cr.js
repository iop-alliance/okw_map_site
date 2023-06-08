function(cluster) {
    var iconSize = new L.Point(20, 20); // Adjust the size of the marker as needed
    var text = cluster.getChildCount(); // Example text to display, you can modify this as per your requirement

    var textX = iconSize.x + 10; // X-coordinate of the text
    var textY = (iconSize.y / 2) + 10; // Y-coordinate of the text

    var circleRadius = iconSize.x / 2; // Radius of the circle
    var circleFill = 'rgba(239, 71, 111, 0.6)'; // Fill color of the circle

    var polylineStartX = circleRadius; // X-coordinate of the polyline start
    var polylineStartY = circleRadius; // Y-coordinate of the polyline start
    var polylineEndX = iconSize.x + 40; // X-coordinate of the polyline end
    var polylineEndY = textY - 10; // Y-coordinate of the polyline end

    var svgContent = `<svg height="${iconSize.y + textY}" width="${iconSize.x + textX}" viewBox="0 0 ${iconSize.x + textX} ${iconSize.y + textY}">
        <circle cx="${circleRadius}" cy="${circleRadius}" r="${circleRadius}" style="fill: ${circleFill};"></circle>
        <text x="${iconSize.x + 20}" y="${iconSize.y / 2}" text-anchor="middle" alignment-baseline="middle" style="fill: black; font-size: 10px;">${text}</text>
        <polyline points="${polylineStartX},${polylineStartY} ${polylineEndX},${polylineEndY}" style="fill: none; stroke: rgba(0,0,0,0.5); stroke-width: 1px;"></polyline>
    </svg>`;

    return L.divIcon({
        html: svgContent,
        className: 'marker-cluster',
        iconSize: [iconSize.x + textX, iconSize.y + textY]
    });
}