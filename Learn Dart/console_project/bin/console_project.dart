import 'package:console_project/console_project.dart' as console_project;

void main(List<String> arguments) {
  try {
    print('Hello world: ${console_project.calculate()}! \n'
        'Args sum: ${arguments.fold<int>(0, (previousValue, element) => previousValue + int.parse(element))}');
  } catch (e) {
    print('Error: At least one argumetn is not an integer!');
  }
}
