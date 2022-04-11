import argparse
import pathlib
import nimbus.poes


def main():
    parser = argparse.ArgumentParser(
        description="Nimbus is a tool for INSERT DESC HERE, DO NOT FORGET"
    )
    parser.add_argument(
        "source", nargs="?", type=pathlib.Path, help="where to process data from"
    )
    parser.add_argument("--wave", dest="wave_file", type=pathlib.Path)
    parser.add_argument("--iq", dest="iq_file", type=pathlib.Path)
    parser.add_argument("--image", dest="image_file", type=pathlib.Path)
    parser.add_argument("--audio", action="store_true")
    parser.add_argument(
        "--sat", choices=["15", "18", "19"], type=str, help="Choice of POES Satellite"
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
