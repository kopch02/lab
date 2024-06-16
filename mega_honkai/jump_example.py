import asyncio
from honkaistarrail import starrail

async def get_jump_history_link():
    link = "https://api-os-takumi.mihoyo.com/common/gacha_record/api/getGachaLog?authkey_ver=1&sign_type=2&lang=ru&authkey=oBWy3z0%2fnDWuYg2RHmOF8Y5YjfkATxAymOHQyrlwP8DimfL7acDyP42mXceJ41JfmLW6RnDpmr4oH5MWfnq26zimVn82KyRMpG3Weav7e8QN7BucCBYyYnoVKXKYo8Y5Aomr3W1Ec7X%2bAq%2ftHfpgjoAOLP7hJr0g%2fKb%2flerlEMjRtSWEiy5reinfKKi18Qw7uvqKQptfYq6YP2tS4Z7qU9F1q7RnHXJ2R5orll4rLhsla8keMP28ycVKNwnppysao%2bp%2bEj778KmPjuDEgN2uDV%2b37x%2bAy6pKP%2bMCZJf02qRHrRUBiPkkc95l8r7S4qcs%2f3jyx3b4Ns%2bZRKfV0yEIbQS67T41DUI8tIEdozyNEBeRst3esfOOauyyFHCOgL1yZoErv%2fbbJYWcfGk%2f9ILoLAqrL%2fYPe6XBN7WG9oh7h3nLNY3gun5bu%2b8PGwV1r4TXJRC1ZHtTfvnM7%2fwkYo%2fiZpSMAF%2fFaPoeRIK7ER%2bho4LM6ysUaqcpkgPHOrC9J6oZ5TVmEi57L3CbO%2baRWgZE9UG4UO91C9Mxa3IxVrKyYMqb4dDvs2YHKksym%2fcI1d2pWKAvvQJRcezGF1XorNUzJkTiswNe6UumRcQUnt%2fwG5VGX6S0Ezba3NjA30vqY9dPKFwXdQ05HgmcGwzWWweogFkyO9x1IJ4ucVL%2fgnqu%2bsw%3d&game_biz=hkrpg_global"
    async with starrail.Jump(link = link,banner = 1,lang = "ru") as hist:
        async for key in hist.get_history():
            for info in key:
                print(f'[{info.type}] Name: {info.name} ({info.rank}*) - {info.time.strftime("%d.%m.%Y %H:%M:%S")}')


async def get_jump_history():
    async with starrail.Jump(banner = 3,lang = "ru") as hist:
        async for key in hist.get_history():
            for ii in key:
                if ii.name == 'Рог изобилия':
                    print(ii)
            #for info in key:
                #print(f'[{info.type}] Name: {info.name} ({info.rank}*) - {info.time.strftime("%d.%m.%Y %H:%M:%S")}')


asyncio.run(get_jump_history())

