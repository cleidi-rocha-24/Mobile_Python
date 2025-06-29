# import logging
# import os
#
#
# def setup_logger(name):
#     logger = logging.getLogger(name)
#     logger.setLevel(logging.INFO)
#
#     # Cria diretório de logs se não existir
#     if not os.path.exists('logs'):
#         os.makedirs('logs')
#
#     # Handler para arquivo
#     file_handler = logging.FileHandler('logs/execution.log')
#     file_handler.setLevel(logging.INFO)
#
#     # Handler para console
#     console_handler = logging.StreamHandler()
#     console_handler.setLevel(logging.INFO)
#
#     # Formato
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     file_handler.setFormatter(formatter)
#     console_handler.setFormatter(formatter)
#
#     # Adiciona handlers
#     logger.addHandler(file_handler)
#     logger.addHandler(console_handler)
#
#     return logger