
def main():
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    out_file = '{}/HelloWorld.txt'.format(dir_path)
    with open(out_file, 'a') as the_file:
        the_file.write('It works!\n')

    import time
    print(time.time())
    with open(out_file, 'a') as the_file:
        the_file.write('It Still works!\n')

    import sys
    print(sys.version)
    print(sys.version_info)

    print('You should see this #1')
    try:
        import __phello__
    except Exception as e:
        print(Exception, e)
        print('You should NOT see this!!!!')
    finally:
        print('You should see this #2')


if __name__ == '__main__':
    main()


