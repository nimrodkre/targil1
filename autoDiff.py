import os
import sys
from exrex import generate, count

dir_path = os.path.dirname(os.path.realpath(__file__))

reference = "~labcc2/www/ex1/school_solution"
coding_style = "~labcc2/www/codingStyleCheck"
pre_submit = "~labcc2/www/ex1/presubmit_ex1"
source = "main.c"

auto_tester_enabled = True
OVERFLOW_ABORT = 20  # 0 == off
AUTO_TESTER = ("best|merge|quick", "((([01]|111|11|1a)11111111,abcd AB-CD[4$]{0,1},(100|0|47|200|\-1),(100|0|47|200|\-1)(,abc\-\-AGC[ 4$]{0,1}D){1,2}\n){0,1}|(1111111111,bb,(100|0|47),(100|47),count,city\n){0,1}(1111111111,ac,(100|0|47),(100|47),count,city\n){0,1}(1111111111,(ba|dd),(100|0|47),(100|47),count,city\n){0,1}(1111111111,ab,(100|0|47),(100|47),count,city\n){0,1})q\n")

TO_COMPILE = ('.c')
COMPILED_NAME = "compiled_test"
UNCOMPILED_NAME = "manageStudents.c"
TAR_NAME = "ex1.tar"
PLACE_HOLDER = "§§§±±±§§§"

SHOW_CURRENT_TEST = False

MANUAL_TESTS = {
	("best",
	 "3888914775,Itzel Gardner,21,26,Iran,Tehran\n5496060426,Korbin Murillo,4,30,Pakistan,Islamabad\n3845354610,Rhett Vargas,98,29,United-Kingdom,London\nq\n"),
	("merge",
	 "3888914775,Itzel Gardner,21,26,Iran,Tehran\n5496060426,Korbin Murillo,4,30,Pakistan,Islamabad\n3845354610,Rhett Vargas,98,29,United-Kingdom,London\nq\n"),
	("quick",
	 "3888914775,Itzel Gardner,21,26,Iran,Tehran\n5496060426,Korbin Murillo,4,30,Pakistan,Islamabad\n3845354610,Rhett Vargas,98,29,United-Kingdom,London\nq\n"),
	("best x", ""),
	("x x", ""),
	("", ""),
	("best", "\nq\n"),
	("best", ",\nq\n"),
	("best", ",,\nq\n"),
	("best", ",,,\nq\n"),
	("best", ",,,,\nq\n"),
	("best", ",,,,,\nq\n"),
	("best", "0888914775,Itzel Gardner,21,26,Iran,Tehran\nq\n"),
	("best", "0888914775,Itzel Gardner,0,26,Iran,Tehran\nq\n"),
	("best", "0888914775,Itzel Gardner,021,26,Iran,Tehran\nq\n"),
	("best", "0888914775,Itzel Gardner,21,026,Iran,Tehran\nq\n"),
	("best", "3888914775,It2zel Gardner,21,26,Iran,Tehran\nq\n"),
	("best", "3888914775,Itzel Gardner,-21,26,Iran,Tehran\nq\n"),
	("best", "3888 914775,Itzel Gardner,21,26,Iran,Tehran\nq\n"),
	("best", "3888914775,Itzel Gardner,21,26,Iran,Teh ran\nq\n"),
	("best", "3888914775,Itzel Gardner,221,26,Iran,Tehran\nq\n"),
	("best", "3888914775,Itzel Gardner,21,2,Iran,Tehran\nq\n"),
	("best", "3888914775,Itzel Gardner,21,202,Iran,Tehran\nq\n"),
	("best", "3888914775,Itzel Gardner,21,26,Ir an,Tehran\nq\n"),
	("best", "3888914775,Itzel Gardner,21,26,Iran,Te hran\nq\n"),
	("best", "3888914775,Itz-el Gardner,21,26,I-ran,Teh-ran\nq\n"),
	("best", "3888914775,Itzel Gardner,21,26,Ir-an,Tehran\nq\n"),
	("best", "3888914775,Itzel Gardner,21,26,Iran,Tehr-an\nq\n"),
	("best", "3888914775,Itzel Gardner,21,26,Iran,Tehran\nq\n"),
	("best", "3d888914775,Itzel Gardner,21,26,Iran,Tehran\nq\n"),
	("best", "1113888914775,Itzel Gardner,21,26,Iran,Tehran\nq\n"),
	("best", "88914775,Itzel Gardner,21,26,Iran,Tehran\nq\n"),
	("best", "3888914775,Itzel Gardner,21,26,Iran,Tehran\nq\n"),
	("best", "3888914775,Itzel Gardner,21,26,IranTehran\nq\n"),
	("best", "3888914775,Itzel Gardner,21,-26,Iran,Tehran\nq\n"),
	("best", "3888914775,Itzel Gardner,21,26,Iran,Tehra4n\nq\n"),
	("best", "3888914775,Itzel Gardner,21,26,Iran,Tehra$n\nq\n"),
	("best", "3888914775,Itzel Gardner,21,26,Ira4n,Tehran\nq\n"),
	("best", "3888914775,Itzel Gardner,21,26,Ira$n,Tehran\nq\n"),
	("best", "3888914775,Itzel Gardner,21,26,Ira$n,Teh4ran\nq\n"),
	("best", "3888914775,Itzel Gardner,21345345345345,26,Iran,Tehran\nq\n"),
	("best", "3888914775,Itzel Gardner,4294967296,26,Iran,Tehran\nq\n"),
	("best",
	 "3888914775,Itzel Gardner,21,26,Iran,Tehran\n5496060426,Korbi$n Murillo,4,30,Pakistan,Islamabad\n3845354610,Rhett Vargas,98,29,United-Kingdom,London\nq\n"),
	("best",
	 "3888914775,Itzel Gardner,21,26,Iran,Tehran\n5496060426,Korbi$n Murillo,4,30,Pakistan,Islamabad\n3845354610,Rhett Va$rgas,98,29,United-Kingdom,London\nq\n"),
	("best",
	 "3888914775,Itzel Gardner,21,0,Iran,Tehran\n5496060426,Korbin Murillo,0,30,Pakistan,Islamabad\n3845354610,Rhett Vargas,98,29,United-Kingdom,London\nq\n"),
	("merge",
	 "3888914775,Itzel Gardner,21,26,Iran,Tehran\n5496060426,Korbin Murillo,21,26,Pakistan,Islamabad\n3845354610,Rhett Vargas,98,29,United-Kingdom,London\nq\n"),
	("quick",
	 "3888914775,Itzel Gardner,21,26,Iran,Tehran\n5496060426,Korbin Murillo,21,26,Pakistan,Islamabad\n3845354610,Rhett Vargas,98,29,United-Kingdom,London\nq\n"),
	("best",
	 "3888914775,Itzel Gardner,21,26,Iran,Tehran\n5496060426,Korbin Murillo,21,26,Pakistan,Islamabad\n3845354610,Rhett Vargas,98,29,United-Kingdom,London\nq\n"),
	("best",
	 "3888914775,Itzel Gardner,21,26,Iran,Tehran\n5496060426,Korbin Murillo,4,30,Pakistan,Islamabad\n3845354610,Rhett Vargas,98,29,United-Kingdom,London\n" * 10 + "q\n"),
	("merge",
	 "3888914775,Itzel Gardner,21,26,Iran,Tehran\n5496060426,Korbin Murillo,4,30,Pakistan,Islamabad\n3845354610,Rhett Vargas,98,29,United-Kingdom,London\n" * 10 + "q\n"),
	("quick",
	 "3888914775,Itzel Gardner,21,26,Iran,Tehran\n5496060426,Korbin Murillo,4,30,Pakistan,Islamabad\n3845354610,Rhett Vargas,98,29,United-Kingdom,London\n" * 10 + "q\n"),
	("best",
	 "3888914775,Itzel Gardner,21,26,Iran,Tehran\n5496060426,Korbin Murillo,4,30,Pakistan,Islamabad\n3845354610,Rhett Vargas,98,29,United-Kingdom,London\n" * 100 + "q\n"),
	("merge",
	 "3888914775,Itzel Gardner,21,26,Iran,Tehran\n5496060426,Korbin Murillo,4,30,Pakistan,Islamabad\n3845354610,Rhett Vargas,98,29,United-Kingdom,London\n" * 100 + "q\n"),
	("quick",
	 "3888914775,Itzel Gardner,21,26,Iran,Tehran\n5496060426,Korbin Murillo,4,30,Pakistan,Islamabad\n3845354610,Rhett Vargas,98,29,United-Kingdom,London\n" * 100 + "q\n"),
	("best",
	 "3888914775,Itzel Gardner,21,26,Iran,Tehran\n5496060426,Korbin Murillo,4,30,Pakistan,Islamabad\n3845354610,Rhett Vargas,98,29,United-Kingdom,London\n" * 1000 + "q\n"),
	("merge",
	 "3888914775,Itzel Gardner,21,26,Iran,Tehran\n5496060426,Korbin Murillo,4,30,Pakistan,Islamabad\n3845354610,Rhett Vargas,98,29,United-Kingdom,London\n" * 1000 + "q\n"),
	("quick",
	 "3888914775,Itzel Gardner,21,26,Iran,Tehran\n5496060426,Korbin Murillo,4,30,Pakistan,Islamabad\n3845354610,Rhett Vargas,98,29,United-Kingdom,London\n" * 1000 + "q\n"),
	("best",
	 "3888914775,Itzel Gardner,21,26,Iran,Tehran\n5496060426,Korbin Murillo,4,30,Pakistan,Islamabad\n3845354610,Rhett Vargas,98,29,United-Kingdom,London\n" * 1833 + "q\n"),
	("merge",
	 "3888914775,Itzel Gardner,21,26,Iran,Tehran\n5496060426,Korbin Murillo,4,30,Pakistan,Islamabad\n3845354610,Rhett Vargas,98,29,United-Kingdom,London\n" * 1833 + "q\n"),
	("quick",
	 "3888914775,Itzel Gardner,21,26,Iran,Tehran\n5496060426,Korbin Murillo,4,30,Pakistan,Islamabad\n3845354610,Rhett Vargas,98,29,United-Kingdom,London\n" * 1833 + "q\n"),
	("best", "q\n")
}


def command(tup):
	return "(" + tup[0] + ")" + PLACE_HOLDER + "(" + tup[1] + ")"


t_count = count(command(AUTO_TESTER))


def run_tests(test_pool, ph=PLACE_HOLDER, overflow_abort=OVERFLOW_ABORT):
	failed = 0
	passed = 0
	errors = []
	for test in test_pool:
		# printf 'input' | comm param > output
		if type(test) is tuple:
			s = test
		else:
			s = test.split(ph, 1)
		if SHOW_CURRENT_TEST:
			print(s)
		out1 = os.system("printf '" + s[1] + "' | " + reference + " " + s[0] + " > expected")
		out2 = os.system("printf '" + s[1] + "' | " + source + " " + s[0] + " > actual")
		os.system("diff -c " + dir_path + "/expected " + dir_path + "/actual > diffs")
		with open("diffs", "r") as d:
			err = d.read()
			if err != "":
				errors.append({
					"test": s,
					"err": err
				})
				failed += 1
			elif out2 != out1:
				errors.append({
					"test": test,
					"err": "different exit status:\nexpected: " + str(out1) + "\ngot: " + str(out2)
				})
				failed += 1
			else:
				passed += 1

		if (failed + passed) % 1000 == 0:
			tot = failed + passed
			if tot >= 5000 and overflow_abort > 0:
				overflow_abort = 10
			print("Calculated", tot, "(", round((tot) * 100.0 / t_count, 2), "%) tests with", failed, "fails.")
		if 0 < overflow_abort <= failed:
			print("There are too many failed tests, aborting...")
			break
	return errors, failed, passed


def count_errors(type, failed, passed):
	total = failed + passed
	score = passed / total
	if failed == 0:
		c_print("Passed all " + str(total) + " " + type + " tests!", 'G')
	else:
		print(c_str(str(failed) + " failed tests", 'R') +
			  " out of " + str(total) + " " + type +
			  " tests (" + c_str(str(round(score * 100)) + "%", 'Y') + ")")


def list_errors(type, errors):
	for i, error in enumerate(errors):
		c_print("---" + type.upper() + " ERROR " + str(i + 1) + "---", 'R')
		print("args:  ", common_filter(error["test"][0]))
		print("input: ", common_filter(error["test"][1]))
		print("Description:\n" + error["err"])


def c_str(str, c):
	# adds some color to the text!
	colors = {
		'Y': "\033[93m{}\033[00m",
		'B': "\033[96m{}\033[00m",
		'G': "\033[92m{}\033[00m",
		'R': "\033[91m{}\033[00m"
	}
	if c not in colors.keys():
		return str
	return colors[c].format(str)


def c_print(str, color):
	# print colored text
	print(c_str(str, color))


def common_filter(str):
	# replace common strings with reader friendly text
	if str == "":
		return "[EMPTY]"
	if str == "\n":
		return "[NEW_LINE]"
	return str


def str_to_bool(s):
	if s.upper() in {'TRUE', 'T'}:
		return True
	elif s.upper() in {'FALSE', 'F'}:
		return False
	else:
		raise ValueError


if __name__ == "__main__":
	if len(sys.argv) >= 2:
		source = sys.argv[1]
	if len(sys.argv) >= 3:
		auto_tester_enabled = str_to_bool(sys.argv[2])
	if os.path.isfile(source):
		if source.endswith(TO_COMPILE):
			c_print("Running pre-submit tests", 'B')
			if source != UNCOMPILED_NAME:
				os.system("cp " + source + " " + UNCOMPILED_NAME)
			os.system("tar -cvf " + TAR_NAME + " " + UNCOMPILED_NAME)
			os.system(pre_submit + " " + TAR_NAME)
			c_print("Running coding style tests", 'B')
			os.system(coding_style + " " + source)
			c_print("Compiling " + source + " as " + COMPILED_NAME, 'B')
			os.system("gcc -Wall -Wvla -Wextra -std=c99 -lm " + source + " -o " + COMPILED_NAME)
			source = COMPILED_NAME

		err_m, f1, s1 = run_tests(MANUAL_TESTS)

		count_errors("manual", f1, s1)

		list_errors("manual", err_m)

		if auto_tester_enabled and f1 == 0:
			c_print("autotester is calculating " + str(t_count) + " tests, please be patient!", 'B')
			err_a, f3, s3 = run_tests(generate(command(AUTO_TESTER)))
			count_errors("automatic", f3, s3)
			list_errors("automatic", err_a)
	else:
		c_print("Source file doesn't exist", 'R')
