
'''
*Al seleccionar una tienda se mostrará:
Una tabla con la información de la tienda.
-Debajo de esa tabla:
total de facturación
total de gastos del personal
mes con mayor facturación

*Al seleccionar un mes se mostrará:
Una tabla con los datos de ese mes.
-Debajo de esa tabla:
media de facturación de todas las tiendas
Tienda con mayor gasto de personal
'''
import polars as pl

df = pl.read_csv("ventas_tiendas.csv")

def tiendas():
    return df["nombre_tienda"].unique().to_list()

def meses():
    return df["mes"].unique().to_list()

#----# funciones relacionadas al 1er cuadro #----#
def datos_tabla_tienda(tienda):
    return df.filter(pl.col("nombre_tienda") == tienda).to_dicts()

def datos_tienda(tienda):
    return df.filter(pl.col("nombre_tienda") == tienda).select(pl.col("facturacion").sum().alias("facturacion_total"),
                                                               pl.col("gastos_personal").sum().alias("gastos_totales")).to_dicts()
def mes_mayor_facturacion(tienda):
    return df.filter(pl.col("nombre_tienda") == tienda).sort(by="gastos_personal", descending=True).row(0)

#----# funciones relacionadas al 2do cuadro #----#
def datos_tabla_mes(mes):
    return df.filter(pl.col("mes") == mes).to_dicts()

def media_facturacion(mes):
    return df.filter(pl.col("mes") == mes).select(pl.col("facturacion").mean().alias("facturacion_media")).to_dicts()

def mayor_gasto_personal(mes):
    return df.filter(pl.col("mes") == mes).sort(by="gastos_personal", descending=True).row(0)

'''
import polars as pl

def ver_tiendas():
    return df.selct(pl.col(df.collect_schema().names()[0])
                    .unique()).collect().to_series().to_list()

def ver_mes():
    return df.selct(pl.col(df.collect_schema().names()[1])
                .unique()).collect().to_series().to_list()

def carga_datos(ruta="ventas.csv"):
    return pl.read_csv(ruta, "ventas.csv", encoding="UTF-8")

def lista_tiendas(df):
    return df["nombre_tienda"].unique().sort().to_list(),

def lista_meses(df):
    return df["mes"].unique().to_list()

-----------Al seleccionar una tienda----------------

def datos_tienda(df,tienda):
    return df.filter(pl.col("nombre_tienda")==tienda)

def total_facturacion(df_tienda):
    return df_tienda["facturacion"].sum()

def total_gastos_personal(df_tiendas):
    return df_tienda["gasto_personal"].sum()
    
def mes_mayor_facturacion(df_tienda):
    return df_tienda.sort("facturacion", descending=True)["mes"][0]

-----------Al seleccionar un mes--------------------
def datos_mes(df, mes):
    return df.filter(pl.col("mes")==mes)

def media_facturacion(df_mes):
    return df_mes["facturacion"].mean()

def tienda_mayor_gasto_personal(df_mes):
    return df_mes.sort("gastos_personal" descending=True)["nombre_tienda"][0]
'''