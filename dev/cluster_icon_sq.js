function(cluster) {
    var iconSize = new L.Point(20, 20); // Adjust the size of the marker as needed
    var text = cluster.getChildCount(); // Example text to display, you can modify this as per your requirement

    var textX = iconSize.x + 10; // X-coordinate of the text
    var textY = iconSize.y / 2; // Y-coordinate of the text

    var rectWidth = iconSize.x; // Width of the rectangle
    var rectHeight = iconSize.y; // Height of the rectangle
    var rectCornerRadius = 2; // Rounded corner radius of the rectangle
    var rectFill = 'rgba(71, 0, 99, 0.6)'; // Fill color of the rectangle

    var polylineStartX = iconSize.x / 2; // X-coordinate of the polyline start
    var polylineStartY = iconSize.y / 2; // Y-coordinate of the polyline start
    var polylineEndX = iconSize.x + 40; // X-coordinate of the polyline end
    var polylineEndY = textY; // Y-coordinate of the polyline end

    var svgContent = `<svg height="${iconSize.y + textY}" width="${iconSize.x + textX}" viewBox="0 0 ${iconSize.x + textX} ${iconSize.y + textY}">
        <rect x="0" y="0" width="${rectWidth}" height="${rectHeight}" rx="${rectCornerRadius}" ry="${rectCornerRadius}" style="fill: ${rectFill};"></rect>
        <text x="${iconSize.x + 20}" y="${iconSize.y / 2}" text-anchor="middle" alignment-baseline="middle" style="fill: black; font-size: 10px;">${text}</text>
        <polyline points="${polylineStartX},${polylineStartY} ${polylineEndX},${polylineEndY}" style="fill: none; stroke: rgba(0,0,0,0.5); stroke-width: 1px;"></polyline>
    </svg>`;

    return L.divIcon({
        html: svgContent,
        className: 'marker-cluster',
        iconSize: [iconSize.x + textX, iconSize.y + textY]
    });
}
