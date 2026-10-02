# Quiz 00

See the instructions in the `assignment` folder for each problem.

For open-ended questions, write your answer where indicated. For multiple-choice questions, uncomment all code lines in exactly one choice per part. Leave the other choices commented out; you do not need to edit the helper modules or tests.

Use Python 3.13 or newer and uv. Run the following commands from the repository root to install dependencies and test your work:

```bash
uv sync --locked
uv run pytest
```

All six tests are expected to fail until you select answers. Each test covers one 5-point part of Problems 01–03. Problem 00 is graded manually for 10 points, for a total of 40 points. To test a single problem, run, for example, `uv run pytest tests/test_problem_02.py`.

To run an individual problem, use its module name from the repository root:

```bash
uv run python -m assignment.problem_01
uv run python -m assignment.problem_02
uv run python -m assignment.problem_03
```

Problem 03 displays a dataset plot. Close the plot window to continue; the script saves `dataset.jpg` and `nn_output.jpg` in the repository root.

To check code style and imports, run `uvx ruff check .` and `uvx ruff format --check .`.

## License

This repository is provided with an MIT license. See the `LICENSE` file.

## Contributing

Please email Mauro Sanchirico at ms3978@camden.rutgers.edu (academic) or sanchirico.mauro@gmail.com (personal) with questions, comments, bug reports, or suggestions for improvement.

