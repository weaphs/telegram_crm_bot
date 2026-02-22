#bot/g_services/g_services
import asyncio
import gspread
from typing import Union, List
from settings.settings import settings

class GoogleSheet:
    def __init__(self):
        self.client = gspread.service_account(filename=settings.GOOGLE_CREDENTIALS_PATH)
        self.spreadsheet = self.client.open(settings.GOOGLE_SHEET_NAME)
        self.client_worksheet=self.spreadsheet.worksheet("Clients")
        self.order_worksheet = self.spreadsheet.worksheet('Order_list')
        self.black_list_worksheet = self.spreadsheet.worksheet('Blocked_users')

    async def add_client(self,data: dict):
        data_list = [value for value in data.values()]
        await asyncio.to_thread(self.client_worksheet.append_row, data_list)

    async def check_client_exist(self,user_id: str)->bool:
        if await asyncio.to_thread(self.client_worksheet.find, user_id):
            return True
        else: return False

    async def get_name(self, user_id: str) -> str | None:
        try:
            cell = await asyncio.to_thread(self.client_worksheet.find, user_id)
            if not cell:
                return None

            address_cell = await asyncio.to_thread(
                self.client_worksheet.cell, cell.row, 1
            )
            return address_cell.value

        except Exception as e:
            print(f"Error in get_address: {e}")
            return None

    async def get_address(self, user_id: str) -> str | None:
        try:
            cell = await asyncio.to_thread(self.client_worksheet.find, user_id)
            if not cell:
                return None

            address_cell = await asyncio.to_thread(
                self.client_worksheet.cell, cell.row, 3
            )
            return address_cell.value

        except Exception as e:
            print(f"Error in get_address: {e}")
            return None

    async def add_order(self,user_id:str,address: str, water_amount:str, date_time:str )->bool:
        name = await self.get_name(user_id)
        data_list = [user_id, name ,address,water_amount, date_time]
        try:
            await  asyncio.to_thread(self.order_worksheet.append_row,data_list)
            return True
        except Exception as e:
            return False

    async def get_profile(self, user_id:str)->Union[List,bool]:
        try:
            cell = await asyncio.to_thread(self.client_worksheet.find,user_id)
            row_num = cell.row
            return await asyncio.to_thread(self.client_worksheet.row_values,row_num)
        except Exception as e:
            print(f"my_orders error: {e}")
            return False

    async def my_orders(self, user_id:str)->list|bool:
        try:
            cell = await asyncio.to_thread(self.order_worksheet.findall,user_id)
            rows = [el.row for el in cell ]
            data = list()
            for row in rows:
                data.append(await asyncio.to_thread(self.order_worksheet.row_values,row))
            return data
        except Exception as e:
            print(f"my_orders error: {e}")
            return False

    async def check_blacklist(self, user_id: str) -> bool:
        try:
            cell = await asyncio.to_thread(self.black_list_worksheet.find,user_id)
            return bool(cell)
        except:
            return False

google_sheet = GoogleSheet()