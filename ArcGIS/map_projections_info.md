# Map Projection Families

### Sources: 
- [Compare Map Projections](https://map-projections.net/imglist.php)
- [Visualize Projections in Motion](https://www.jasondavies.com/maps/transition/)
- [Explanation of Projections Video](https://www.youtube.com/watch?v=bpp0xCknQAQ&ab_channel=KuvinaSaydaki)

### Cylindric (Cylindrical Projection)
The Earth's surface is projected onto a cylinder. When unwrapped, the map shows the meridians (lines of longitude) as straight, equally spaced vertical lines and the parallels (lines of latitude) as straight horizontal lines.  
**Example**: Mercator projection.  
**Uses**: Useful for navigation because straight lines on the map correspond to constant compass bearings (rhumb lines).

### Pseudocylindric (Pseudocylindrical Projection)
A variant of cylindrical projections but with curved meridians. The central meridian is a straight line, but other meridians are curved.  
**Example**: Mollweide projection.  
**Uses**: Often used for world maps where preserving relative area is important.

### Conic (Conical Projection)
The Earth is projected onto a cone that touches or intersects the globe. Parallels appear as arcs, and meridians radiate from a central point.  
**Example**: Albers Equal-Area Conic.  
**Uses**: Common for regional maps of mid-latitude areas.

### Lenticular (Lens-Shaped Projection)
These projections produce maps that resemble a lens or an oval shape. They are usually specific types of pseudocylindrical projections.  
**Example**: Sinusoidal projection.  
**Uses**: Often used for thematic or educational world maps.

### Azimuthal (Planar Projection)
The Earth is projected onto a flat plane. Typically, these projections are centered on one point (e.g., the North or South Pole), so distances and directions are accurate from the center point.  
**Example**: Stereographic or Orthographic projection.  
**Uses**: Ideal for polar maps and for showing the globe from a specific viewpoint.

### Polyhedral Projection
The Earth's surface is projected onto a polyhedron (a multi-sided 3D shape like a cube or icosahedron), which is then unfolded into 2D. Each face of the polyhedron is typically mapped using a different projection.  
**Example**: Fuller (Dymaxion) projection.  
**Uses**: Novel designs intended to minimize distortion over the entire map.

### Miscellaneous Projections
Projections that do not fit into the standard categories. They are often experimental or unique, serving very specific purposes.  
**Example**: Goode's Interrupted Homolosine projection.  
**Uses**: Useful for thematic maps where specific regions or features are emphasized.

### Planar (Azimuthal)
Planar projections (a broader category that includes azimuthal) project the Earth onto a flat plane. There are non-azimuthal variants like:  
**Example**: Gnomonic projection (used for plotting the shortest path between points on the globe).

### Interrupted Projections
These are projections where the map is "interrupted" in certain places (e.g., oceans), reducing distortion over landmasses.  
**Example**: Goode’s Homolosine projection.  
**Uses**: Emphasizes landforms while minimizing distortion, often for world maps.

### Retroazimuthal Projections
Directions from any point on the map to a fixed location are correct.  
**Example**: Craig retroazimuthal projection.  
**Uses**: Navigational maps where direction is important from any location to a fixed point, such as a pilgrimage map.

### Tangent and Secant Projections
These are projections where the projection surface either touches the globe at a single line (tangent) or intersects it along two lines (secant), reducing distortion along those lines.  
**Uses**: Regional or national maps with accuracy along certain latitudes or longitudes.

# Projection Properties

### Conformal
Preserves the local shape of geographic features. Angles are maintained, but area may be distorted.  
**Example**: Mercator projection.  
**Uses**: Navigation and meteorology.

### Equidistant
Preserves distances from a specific point or along specific lines (such as meridians or parallels), though true distances are not maintained everywhere.  
**Example**: Azimuthal equidistant projection.  
**Uses**: Radio and seismic plotting.

### Equal-Area
Preserves area, meaning regions on the map have the correct proportions relative to one another. Shape and distance may be distorted.  
**Example**: Gall-Peters projection.  
**Uses**: Maps where relative land area is important, such as population density or resource maps.

### Compromise
A balance between different distortions (shape, area, distance) to create a visually appealing and balanced map. No property is perfectly preserved, but no property is heavily distorted either.  
**Example**: Robinson projection.  
**Uses**: General-purpose world maps.

### Gnomonic
Ensures that all great circles (the shortest paths between two points on the globe) are straight lines on the map.  
**Example**: Gnomonic projection.  
**Uses**: Navigational charts for air and sea travel, where plotting the shortest route is important.

### Perspective
Some projections mimic the way the Earth would look from a specific perspective (like from space or an aircraft).  
**Example**: Orthographic projection (mimics the view of a globe from infinite distance).  
**Uses**: Visualization of global views and celestial maps.

### Non-Projective (Non-Mathematical)
These projections don’t follow strict mathematical rules and may be artistic or manually adjusted to minimize distortion in certain regions.  
**Example**: AuthaGraph projection.  
**Uses**: Educational or artistic maps.

### Tissot's Indicatrix
Not a projection but a tool used to visually represent distortions. It shows how scale, shape, and angle distortion vary across a map.  
**Uses**: Helps cartographers understand the effects of distortion on different projections.
