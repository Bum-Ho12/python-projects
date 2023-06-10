from multiprocessing import Pool

#callback function for pool.apply_async
def collect_results(result):
    print('In collect_results: ', result)

def worker(x):
    print('In worker with: ',x,'\n')
    return x*x

def main():
    with Pool(processes=4) as pool:
        ##with print orderly
        # print(pool.map(worker,[0,1,2,3,4,5]))
        ## print unordered
        # for result in pool.imap_unordered(
        #     worker,[0,1,2,3,4,5]
        # ):
        #     print('result: ',result,'\n')

        ## apply async synchronization
        # with get
        with Pool(processes=2) as pool:
            res = pool.apply_async(worker,[6])
            print('Result from async: ',res.get(timeout=1))

        # with callback
        with Pool(processes=2) as pool:
            pool.apply_async(
                worker,args=[4],
                callback = collect_results
            )


if __name__ == '__main__':
    main()