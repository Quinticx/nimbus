import argparse
import pathlib
import nimbus.poes


def main():
    parser = argparse.ArgumentParser(
        description="Nimbus is a tool for processing satellite data"
    )
    parser.add_argument(
        "source",
        nargs="?",
        type=pathlib.Path,
        help="Where to process data from. Can be an .iq or .wav file. If ommitedd, the SDR is assumed to be the source",
    )
    parser.add_argument(
        "--wave",
        dest="wave_file",
        type=pathlib.Path,
        help="Path to save AM intermediate signal to. If omitted, signal is not saved",
    )
    parser.add_argument(
        "--iq",
        dest="iq_file",
        type=pathlib.Path,
        help="Path to save unprocessed signal to. If omitted, signal is not saved",
    )
    parser.add_argument(
        "--image",
        dest="image_file",
        type=pathlib.Path,
        help="Path to save final output signal to. If omitted, signal is not saved",
    )
    parser.add_argument(
        "--audio", action="store_true", help="Preview audio while processing"
    )
    parser.add_argument(
        "--sat",
        default="15",
        choices=["15", "18", "19"],
        type=str,
        help="Choice of POES Satellite",
    )

    args = parser.parse_args()
    frequency = nimbus.poes.id_to_freq(args.sat)
    pipeline = None

    if args.source is None:
        pipeline = nimbus.poes.pipeline(
            True,
            None,
            None,
            args.iq_file,
            args.wave_file,
            args.image_file,
            args.audio,
            frequency,
        )
    elif args.source.suffix == ".iq":
        pipeline = nimbus.poes.pipeline(
            False,
            args.source,
            None,
            args.iq_file,
            args.wave_file,
            args.image_file,
            args.audio,
            frequency,
        )
    elif args.source.suffix == ".wav":
        pipeline = nimbus.poes.pipeline(
            False,
            None,
            args.source,
            args.iq_file,
            args.wave_file,
            args.image_file,
            args.audio,
            frequency,
        )

    pipeline.run()


if __name__ == "__main__":
    main()
