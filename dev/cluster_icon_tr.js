function(cluster) {
        var iconSize = new L.Point(20, 20); // Adjust the size of the marker as needed
        var text = cluster.getChildCount(); // Example text to display, you can modify this as per your requirement

        // Calculate the position of the text beside the SVG icon
        var textX = iconSize.x + 10; // X-coordinate of the text
        var textY = iconSize.y / 2; // Y-coordinate of the text

        // Calculate the position of the polyline
        var lineStartX = (iconSize.x / 2); // X-coordinate of the line start
        var lineStartY = (iconSize.y / 2); // Y-coordinate of the line start
        var lineEndX = (iconSize.x + 40); // X-coordinate of the line end
        var lineEndY = textY; // Y-coordinate of the line end

        return L.divIcon({
            html: '<svg height="' + (iconSize.y + textY) + '" width="' + (iconSize.x + textX) + '" viewBox="0 0 ' + (iconSize.x + textX) + ' ' + (iconSize.y + textY) + '"><polygon points="0,0 ' + (iconSize.x / 2) + ',' + iconSize.y + ' ' + iconSize.x + ',0" style="fill: rgba(0, 166, 118, 0.6);"></polygon><text x="' + (iconSize.x + 20) + '" y="' + (iconSize.y / 2) + '" text-anchor="middle" alignment-baseline="middle" style="fill: black; font-size: 10px;">' + text + '</text><polyline points="' + lineStartX + ',' + lineStartY + ' ' + lineEndX + ',' + lineEndY + '" style="fill: none; stroke: rgba(0,0,0,0.5); stroke-width: 1px;"></polyline></svg>',
            className: 'marker-cluster',
            iconSize: [iconSize.x + textX, iconSize.y + textY]
        });
    }