import plotly.offline as plt
import plotly.graph_objs as go

def plot1D(fuzzyset):

    """

    Draws a 2D plot of a 1D fuzzy set and its membership degrees

    Input:
        fuzzyset: (Type: object "FuzzySet") a fuzzy set

    Output:
        None

    """

    trace = go.Scatter(
        text = "Degrees",
        x = fuzzyset.get_set(),
        y = fuzzyset.get_degrees(),
        mode = 'markers'
    )

    data = [trace]

    layout = dict(
        title = 'Fuzzy sets and its membership degrees',
        xaxis = dict(title = 'Elements'),
        yaxis = dict(title = 'Degrees'),
    )

    fig = dict(data=data, layout=layout)
    
    plt.iplot(fig, filename='fuzzyset.html')


def plot2D(fuzzyset):

    """

    Draws a 3D plot of a 2D set and its membership degrees

    Input:
        set:     (Type: numpy.array)   a 2D fuzzy set
        degrees: (Type: list of reals) membership degrees of the set

    Output:
        None

    """
    pass
    
def plot3D(fuzzyset):

    """

    Draws a 4D plot of a 3D set and its membership degrees

    Input:
        set:     (Type: numpy.array)   a 3D fuzzy set
        degrees: (Type: list of reals) membership degrees of the set

    Output:
        None

    """
    pass
    