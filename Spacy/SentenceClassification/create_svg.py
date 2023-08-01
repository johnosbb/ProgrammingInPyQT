from svgwrite import Drawing, rgb


def create_svg():
    # Create a new SVG drawing
    dwg = Drawing(size=("200px", "100px"))

    # Add a white rectangle as the background
    dwg.add(dwg.rect(insert=("0px", "0px"), size=(
        "200px", "100px"), fill=rgb(255, 255, 255)))

    # Add a text element with "HelloWorld"
    dwg.add(dwg.text("HelloWorld", insert=("50px", "50px"), fill=rgb(0, 0, 0)))

    # Save the SVG to a file
    dwg.saveas("hello_world.svg")


# Create the SVG diagram
create_svg()
