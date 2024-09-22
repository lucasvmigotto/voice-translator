from itertools import batched

from gradio import (
    Audio,
    Blocks,
    Button,
    ClearButton,
    Column,
    Group,
    Row,
    WaveformOptions,
)

from services.voice_to_voice import VoiceToVoice
from utils.settings import settings


_WAVE_FORM_COLOR: str = '#01C6FF'
_WAVE_FORM_PROGRESS: str = '#0066B4'
_LANGUAGES: list[dict[str, str]] = settings.config('app', 'languages')

_voice2voice: VoiceToVoice = VoiceToVoice(settings)


with Blocks() as gui:

    with Row():

        with Column():

            _audio_input = Audio(
                sources=['microphone'],
                type='filepath',
                show_download_button=True,
                waveform_options=WaveformOptions(
                    waveform_color=_WAVE_FORM_COLOR,
                    waveform_progress_color=_WAVE_FORM_PROGRESS,
                    skip_length=2,
                    show_controls=False
                )
            )

            with Row():
                _submit = Button(
                    'Submit',
                    variant='primary'
                )
                _button = ClearButton(
                    _audio_input,
                    'Clear'
                )

    with Row():

        with Column():

            _outputs = []

            for batch in batched(_LANGUAGES, 3):

                with Row():

                    for language in batch:

                        with Group():
                            audio_output = Audio(
                                label=language['label'],
                                interactive=False
                            )
                            _outputs.append(audio_output)


    _submit.click(
        fn=_voice2voice.generate,
        inputs=_audio_input,
        outputs=_outputs,
        show_progress=True
    )
