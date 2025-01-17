import logging
from pathlib import Path

import panel as pn
import param
from panel.io.loading import start_loading_spinner, stop_loading_spinner

from ecodata.app.config import DEFAULT_TEMPLATE
from ecodata.panel_utils import (
    make_mp4_from_frames,
    param_widget,
    register_view,
    try_catch, rename_param_widgets,
)
from ecodata.app.models import FileSelector

logger = logging.getLogger(__file__)


class MovieMaker(param.Parameterized):

    # Frames directory
    frames_dir = param_widget(FileSelector(constrain_path=False, expanded=True))

    # Output file
    output_file = param_widget(
        pn.widgets.TextInput(placeholder="Choose an output file...", value="output.mp4", name="Output file")
    )

    frame_rate = param_widget(
        pn.widgets.EditableIntSlider(name="Frame rate", start=1, end=30, step=1, value=1, sizing_mode="fixed")
    )

    # Go button
    go_button = param_widget(pn.widgets.Button(name="Make movie", button_type="primary", sizing_mode="fixed"))

    # Status
    status_text = param.String("Ready...")

    def __init__(self, **params):
        super().__init__(**params)

        # Reset names for panel widgets
        rename_param_widgets(
            self,
            [
                "frames_dir",
                "output_file",
                "frame_rate",
                "go_button",
            ]
        )

        # Widget groups
        self.movie_widgets = pn.Card(
            self.frames_dir, self.frame_rate, self.output_file, self.go_button, title="Movie maker"
        )

        self.status = pn.pane.Alert(self.status_text)

        # View
        self.view_objects = {"movie_widgets": 0, "status": 1}

        self.alert = pn.pane.Markdown(self.status_text)

        self.view = pn.Column(self.movie_widgets)

    @try_catch()
    @param.depends("status_text", watch=True)
    def update_status_text(self):
        self.alert.object = self.status_text

    @try_catch()
    @param.depends("go_button.value", watch=True)
    def make_movie(self):

        self.status_text = "Creating movie..."
        start_loading_spinner(self.view)
        try:
            output_file = make_mp4_from_frames(
                self.frames_dir.value, self.output_file.value, frame_rate=self.frame_rate.value
            )
            assert output_file.exists()
            self.status_text = f"Movie saved to: {output_file}"

        except Exception as e:
            msg = "Error creating movie...."
            logger.warning(msg + f":\n{e!r}")
            self.status_text = msg
        finally:
            stop_loading_spinner(self.view)


@register_view()
def view():
    viewer = MovieMaker()
    template = DEFAULT_TEMPLATE(
        main=[viewer.alert, viewer.view],
    )
    return template


if __name__ == "__main__":
    pn.serve({Path(__file__).name: view})

if __name__.startswith("bokeh"):
    view()
