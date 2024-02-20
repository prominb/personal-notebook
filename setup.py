from setuptools import setup, find_namespace_packages  # find_packages

setup(
    name='personal-assistant2',
    version='0.0.1',
    description='Personal assistant helps you organize your notes and address book.',
    url='https://github.com/prominb/personal-assistant2',
    author='Olds coders',
    author_email='flyingcircus@example.com',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"],
    packages=find_namespace_packages(where="personal_assistant2"),
    # packages=find_packages(where="personal_assistant2"),
    # package_dir={"": "personal_assistant2"},
    data_files=[('personal_assistant2', ['personal_assistant2/contacts.json', 'personal_assistant2/notes.json'])],
    include_package_data=True,
    package_data={"personal_assistant2": ["*.json", "*.txt"]},
    install_requires=[
        'prompt-toolkit>=3.0'],
    entry_points={'console_scripts': ['run-assistant = personal_assistant2.main:run_bot']},
    zip_safe=False
)
